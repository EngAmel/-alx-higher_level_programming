#include <stdio.h>
#include <Python.h>

/**
 *print_python_list_info - print basic info
 *@p: The list
 */

void print_python_list_info(PyObject *p)
{
	int si, loc, count;
	Pyobject *obj;

	size = Py_SIZE(p);
	loc = ((PyListobject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", si);
	printf("[*] Allocated = %d\n", loc);
	for (count = 0; count < si; count++)
	{
		printf("Element %d: ", loc);
		obj = PyList_GetItem(p, count);
		printf("%s\n", py_TYPE(obj)->tp_name);
	}
}
