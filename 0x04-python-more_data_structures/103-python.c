#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - This func will print the byte info
 *
 * @p: This represents a python Object
 *
 * Return: Nothing
 *
 */

void print_python_bytes(PyObject *p)
{
	long int dSize, item, myLimit;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	dSize = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", dSize);
	printf("  trying string: %s\n", str);

	if (dSize >= 10)
		myLimit = 10;
	else
		myLimit = dSize + 1;

	printf("  first %ld bytes:", myLimit);

	for (item = 0; item < myLimit; item++)
		if (str[item] >= 0)
			printf(" %02x", str[item]);
		else
			printf(" %02x", 256 + str[item]);

	printf("\n");
}

/**
 * print_python_list - This func will print list information
 *
 * @p: This represents a python Object
 *
 * Return: Nothing
 *
 */

void print_python_list(PyObject *p)
{
	long int dSize, item;
	PyListObject *list;
	PyObject *obj;

	dSize = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", dSize);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (item = 0; item < dSize; item++)
	{
		obj = ((PyListObject *)p)->ob_item[item];
		printf("Element %ld: %s\n", item, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
