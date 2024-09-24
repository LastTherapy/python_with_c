#include <Python.h>

// Функция сложения
static PyObject* add(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return PyFloat_FromDouble(a + b);
}

// Функция вычитания
static PyObject* sub(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return PyFloat_FromDouble(a - b);
}

// Функция умножения
static PyObject* mul(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return PyFloat_FromDouble(a * b);
}

// Функция деления (имя изменено на `divide`)
static PyObject* divide(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    if (b == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Division by zero is undefined");
        return NULL;
    }
    return PyFloat_FromDouble(a / b);
}

// Описание функций модуля
static PyMethodDef CalculatorMethods[] = {
    {"add", add, METH_VARARGS, "Add two numbers (int or float)"},
    {"sub", sub, METH_VARARGS, "Subtract two numbers (int or float)"},
    {"mul", mul, METH_VARARGS, "Multiply two numbers (int or float)"},
    {"div", divide, METH_VARARGS, "Divide two numbers (int or float)"},  // Имя изменено
    {NULL, NULL, 0, NULL}
};

// Определение модуля
static struct PyModuleDef calculatormodule = {
    PyModuleDef_HEAD_INIT,
    "calculator",  // имя модуля
    NULL,          // документация модуля (можно оставить NULL)
    -1,            // размер состояния (если модуль сохраняет состояния - можно оставить -1)
    CalculatorMethods
};

// Инициализация модуля
PyMODINIT_FUNC PyInit_calculator(void) {
    return PyModule_Create(&calculatormodule);
}
