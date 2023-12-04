#include <Python.h>

/**
 * print_python_list_info - This func prints
 * basic info about Python lists.
 *
 * @p: This is a PyObject list.
 *
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, ik;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (ik = 0; ik < size; ik++)
	{
		printf("Element %d: ", ik);

		obj = PyList_GetItem(p, ik);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
