#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *object = (PyListObject *)p;
	long size = PyList_Size(p);
	int i;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", object->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
	}
}
