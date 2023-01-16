#!/usr/bin/env python3
# Copyright (C) 2023 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License a
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from python.generators.diff_tests.testing import Path, Metric
from python.generators.diff_tests.testing import Csv, Json, TextProto
from python.generators.diff_tests.testing import DiffTestBlueprint
from python.generators.diff_tests.testing import DiffTestModule


class DiffTestModule_Atrace(DiffTestModule):

  def test_bad_print_textproto_list_slices(self):
    return DiffTestBlueprint(
        trace=Path('bad_print.textproto'),
        query=Path('../common/list_slices_test.sql'),
        out=Csv("""
"ts","dur","name"
74662603048,2,"valid_print"
"""))

  def test_bad_print_systrace_list_slices(self):
    return DiffTestBlueprint(
        trace=Path('bad_print.systrace'),
        query=Path('../common/list_slices_test.sql'),
        out=Csv("""
"ts","dur","name"
10852771242000,3000,"some event"
"""))

  def test_instant_atrace_instant_with_thread(self):
    return DiffTestBlueprint(
        trace=Path('instant_atrace.py'),
        query=Path('instant_with_thread_test.sql'),
        out=Csv("""
"thread_name","track_name","ts"
"t2","t2_event",51
"t1","t1_event",53
"""))

  def test_instant_async_atrace_instant_async(self):
    return DiffTestBlueprint(
        trace=Path('instant_async_atrace.py'),
        query=Path('instant_async_test.sql'),
        out=Csv("""
"process_name","track_name","instant_name","ts"
"p2","track_p2","ev1",51
"p1","track_p1","ev2",53
"""))

  def test_android_b2b_async_begin_list_slices(self):
    return DiffTestBlueprint(
        trace=Path('android_b2b_async_begin.textproto'),
        query=Path('../common/list_slices_test.sql'),
        out=Csv("""
"ts","dur","name"
1000,30,"multistart"
1015,45,"multistart"
1030,20,"multistart"
"""))

  def test_process_track_slices_android_async_slice(self):
    return DiffTestBlueprint(
        trace=Path('android_async_slice.textproto'),
        query=Path('../common/process_track_slices_test.sql'),
        out=Path('process_track_slices_android_async_slice.out'))

  def test_async_track_atrace_process_track_slices(self):
    return DiffTestBlueprint(
        trace=Path('async_track_atrace.py'),
        query=Path('../common/process_track_slices_test.sql'),
        out=Csv("""
"ts","dur","pid","slice_name","track_name"
50,25,1,"ev","track"
55,15,1,"ev","track"
60,5,2,"ev","track"
"""))

  def test_sys_write_and_atrace(self):
    return DiffTestBlueprint(
        trace=Path('sys_write_and_atrace.py'),
        query=Path('sys_write_and_atrace_test.sql'),
        out=Csv("""
"ts","dur","name","depth"
100,100,"sys_write",0
300,50,"sys_write",0
350,300,"test",0
600,50,"sys_write",1
"""))
