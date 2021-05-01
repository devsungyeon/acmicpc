#!/bin/bash
read fn
if [ ! -f c$fn.c ]; then
	echo -e "#include <stdio.h>\n\nint main() {\n\t\n\treturn 0;\n}" > c$fn.c
fi
if [ ! -f cpp$fn.cpp ]; then
	echo -e "#include <bits/stdc++.h>\n\nusing namespace std;\n\nint main() {\n\t\n\treturn 0;\n}" > cpp$fn.cpp
fi
if [ ! -f p$fn.py ]; then 
	echo "" > p$fn.py
fi
if [ ! -f j$fn.java ]; then
	echo -e "import java.util.Scanner;\npublic class j$fn {\n\tpublic static void main(String[] args) {\n\t\t\n\t}\n}" > j$fn.java
fi
