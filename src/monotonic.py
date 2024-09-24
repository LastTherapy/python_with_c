import ctypes, os, sys

__all__ = ["monotonic_time"]

if sys.platform.startswith('linux'):
    # Linux: используем clock_gettime с CLOCK_MONOTONIC_RAW
    CLOCK_MONOTONIC_RAW = 4  # Значение для CLOCK_MONOTONIC_RAW

    class timespec(ctypes.Structure):
        _fields_ = [
            ('tv_sec', ctypes.c_long),  # секунды
            ('tv_nsec', ctypes.c_long)  # наносекунды
        ]

    librt = ctypes.CDLL('librt.so.1', use_errno=True)
    clock_gettime = librt.clock_gettime
    clock_gettime.argtypes = [ctypes.c_int, ctypes.POINTER(timespec)]

    def monotonic_time():
        t = timespec()
        if clock_gettime(CLOCK_MONOTONIC_RAW, ctypes.pointer(t)) != 0:
            errno_ = ctypes.get_errno()
            raise OSError(errno_, os.strerror(errno_))
        return t.tv_sec + t.tv_nsec * 1e-9

elif sys.platform == 'darwin':
    # macOS: используем mach_absolute_time и mach_timebase_info
    class mach_timebase_info_data_t(ctypes.Structure):
        _fields_ = [
            ('numer', ctypes.c_uint32),
            ('denom', ctypes.c_uint32)
        ]

    libc = ctypes.CDLL('/usr/lib/libc.dylib', use_errno=True)

    # Получаем доступ к функции mach_absolute_time
    mach_absolute_time = libc.mach_absolute_time
    mach_absolute_time.restype = ctypes.c_uint64

    # Получаем доступ к функции mach_timebase_info для пересчета тиков
    mach_timebase_info = libc.mach_timebase_info
    mach_timebase_info.argtypes = [ctypes.POINTER(mach_timebase_info_data_t)]

    def monotonic_time():
        # Получаем базовую информацию о времени
        timebase_info = mach_timebase_info_data_t()
        if mach_timebase_info(ctypes.pointer(timebase_info)) != 0:
            errno_ = ctypes.get_errno()
            raise OSError(errno_, os.strerror(errno_))

        # Получаем текущее значение монотонного времени в тиках
        t = mach_absolute_time()

        # Преобразуем тики в наносекунды
        t_ns = t * timebase_info.numer // timebase_info.denom

        # Возвращаем время в секундах
        return t_ns * 1e-9

else:
    raise NotImplementedError("Эта операционная система не поддерживается")

if __name__ == "__main__":
    print(monotonic_time())
