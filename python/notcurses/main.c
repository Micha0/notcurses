// SPDX-License-Identifier: Apache-2.0
/*
Copyright 2020, 2021 igo95862

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

#include <Python.h>

#include "notcurses-python.h"

PyObject *traceback_format_exception = NULL;
PyObject *new_line_unicode = NULL;

static void
Notcurses_module_free(PyObject *Py_UNUSED(self))
{
    Py_XDECREF(traceback_format_exception);
    Py_XDECREF(new_line_unicode);
}

extern PyMethodDef pync_methods[];

static struct PyModuleDef NotcursesMiscModule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "Notcurses",
    .m_doc = "Notcurses python module",
    .m_size = -1,
    .m_methods = pync_methods,
    .m_free = (freefunc)Notcurses_module_free,
};

static PyStructSequence_Field NcInput_fields[] = {
    {"id", "Unicode codepoint or synthesized NCKEY event"},
    {"y", "y cell coordinate of event, -1 for undefined"},
    {"x", "x cell coordinate of event, -1 for undefined"},
    {"utf8", "utf8 representation, if one exists"},
    // Note: alt, shift, ctrl fields deprecated in C API are omitted.
    {"evtype", NULL},
    {"modifiers", "bitmask over NCKEY_MOD_*"},
    {"ypx", "y pixel offset within cell, -1 for undefined"},
    {"xpx", "x pixel offset within cell, -1 for undefined"},
    {NULL, NULL},
};

static struct PyStructSequence_Desc NcInput_desc = {
    .name = "NcInput",
    .doc = "Notcurses input event",
    .fields = NcInput_fields,
    .n_in_sequence = 8,
};

PyTypeObject *NcInput_Type;

PyMODINIT_FUNC
PyInit_notcurses(void)
{
    PyObject *py_module = NULL;
    py_module = PyModule_Create(&NotcursesMiscModule);

    GNU_PY_CHECK_INT(PyModule_AddFunctions(py_module, ChannelsFunctions));
    GNU_PY_CHECK_INT(PyModule_AddFunctions(py_module, MiscFunctions));

    // Type ready?
    GNU_PY_TYPE_READY(&Notcurses_Type);
    GNU_PY_TYPE_READY(&NotcursesOptions_Type);
    GNU_PY_TYPE_READY(&NcPlane_Type);
    GNU_PY_TYPE_READY(&NcPlaneOptions_Type);

    // Add objects
    GNU_PY_MODULE_ADD_OBJECT(py_module, (PyObject *)&Notcurses_Type, "Notcurses");
    GNU_PY_MODULE_ADD_OBJECT(py_module, (PyObject *)&NotcursesOptions_Type, "NotcursesOptions");
    GNU_PY_MODULE_ADD_OBJECT(py_module, (PyObject *)&NcPlane_Type, "NcPlane");
    GNU_PY_MODULE_ADD_OBJECT(py_module, (PyObject *)&NcPlaneOptions_Type, "NcPlaneOptions");

    NcInput_Type = PyStructSequence_NewType(&NcInput_desc);
    if (NcInput_Type == NULL)
        return NULL;
    GNU_PY_MODULE_ADD_OBJECT(py_module, (PyObject *)NcInput_Type, "NcInput");

    // background cannot be highcontrast, only foreground
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCALPHA_HIGHCONTRAST));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCALPHA_TRANSPARENT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCALPHA_BLEND));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCALPHA_OPAQUE));

    // FIXME: Better, attributes of an object such as an enum.
    GNU_PY_CHECK_INT(PyModule_AddStringMacro(py_module, NCBOXASCII));
    GNU_PY_CHECK_INT(PyModule_AddStringMacro(py_module, NCBOXDOUBLE));
    GNU_PY_CHECK_INT(PyModule_AddStringMacro(py_module, NCBOXHEAVY));
    GNU_PY_CHECK_INT(PyModule_AddStringMacro(py_module, NCBOXLIGHT));
    GNU_PY_CHECK_INT(PyModule_AddStringMacro(py_module, NCBOXOUTER));
    GNU_PY_CHECK_INT(PyModule_AddStringMacro(py_module, NCBOXROUND));

    // if this bit is set, we are *not* using the default background color
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NC_BGDEFAULT_MASK));
    // extract these bits to get the background RGB value
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NC_BG_RGB_MASK));
    // if this bit *and* NC_BGDEFAULT_MASK are set, we're using a
    // palette-indexed background color
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NC_BG_PALETTE));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCPALETTESIZE));
    // extract these bits to get the background alpha mask
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NC_BG_ALPHA_MASK));

    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_INVALID));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_RESIZE));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_UP));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_RIGHT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_DOWN));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_LEFT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_INS));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_DEL));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BACKSPACE));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_PGDOWN));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_PGUP));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_HOME));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_END));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F00));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F01));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F02));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F03));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F04));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F05));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F06));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F07));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F08));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F09));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F10));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F11));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F12));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F13));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F14));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F15));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F16));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F17));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F18));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F19));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F20));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F21));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F22));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F23));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F24));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F25));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F26));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F27));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F28));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F29));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F30));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F31));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F32));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F33));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F34));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F35));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F36));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F37));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F38));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F39));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F40));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F41));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F42));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F43));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F44));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F45));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F46));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F47));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F48));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F49));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F50));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F51));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F52));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F53));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F54));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F55));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F56));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F57));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F58));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F59));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_F60));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_ENTER));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_CLS));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_DLEFT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_DRIGHT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_ULEFT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_URIGHT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_CENTER));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BEGIN));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_CANCEL));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_CLOSE));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_COMMAND));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_COPY));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_EXIT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_PRINT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_REFRESH));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_SEPARATOR));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_CAPS_LOCK));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_SCROLL_LOCK));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_NUM_LOCK));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_PRINT_SCREEN));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_PAUSE));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MENU));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_PLAY));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_PAUSE));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_PPAUSE));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_REV));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_STOP));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_FF));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_REWIND));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_NEXT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_PREV));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_RECORD));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_LVOL));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_RVOL));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MEDIA_MUTE));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_LSHIFT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_LCTRL));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_LALT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_LSUPER));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_LHYPER));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_LMETA));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_RSHIFT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_RCTRL));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_RALT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_RSUPER));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_RHYPER));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_RMETA));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_L3SHIFT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_L5SHIFT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MOTION));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON1));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON2));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON3));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON4));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON5));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON6));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON7));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON8));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON9));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON10));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_BUTTON11));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_SIGNAL));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_EOF));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_SCROLL_UP));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_SCROLL_DOWN));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_RETURN));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_TAB));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_ESC));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_SPACE));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MOD_SHIFT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MOD_ALT));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MOD_CTRL));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MOD_SUPER));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MOD_HYPER));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MOD_META));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MOD_CAPSLOCK));
    GNU_PY_CHECK_INT(PyModule_AddIntMacro(py_module, NCKEY_MOD_NUMLOCK));

    PyObject *traceback_module = GNU_PY_CHECK(PyImport_ImportModule("traceback"));
    traceback_format_exception = GNU_PY_CHECK(PyObject_GetAttrString(traceback_module, "format_exception"));
    Py_DECREF(traceback_module);
    new_line_unicode = GNU_PY_CHECK(PyUnicode_FromString("\n"));

    Py_INCREF(py_module);
    return py_module;
}
