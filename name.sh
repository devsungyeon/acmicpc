#!/bin/bash

read  fn
#echo -e "#include <bits/stdc++.h>\n\nusing namespace std;\n\nint main() {\n\t\n\treturn 0;\n}" > $fn.cpp
#echo -e "#include <bits/stdc++.h>\n\nint main() {\n\t\n\treturn 0;\n}" > $fn.cpp
#echo "" > $fn.python
echo -e "public class j$fn {\n\tpublic static void main(String[] args) {\n\t\t\n\t}\n}" > j$fn.java