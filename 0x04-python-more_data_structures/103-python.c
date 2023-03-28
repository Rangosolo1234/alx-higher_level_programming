#include <Python.h>
#include <stdio.h>

/**
 * Prints information about a Python list.
 * 
 * @param p A pointer to a PyObject representing a list.
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("[*] Python list info error\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * Prints information about a Python bytes object.
 * 
 * @param p A pointer to a PyObject representing a bytes object.
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes: ", size < 10 ? size : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx ", str[i]);
    }
    printf("\n");
}
