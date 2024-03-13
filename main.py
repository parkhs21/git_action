content = [
    "[%hardbreaks]\n",
    "test.adoc\n",
    "test.adoc\n"
]

with open("test.adoc", "w") as file:
    for c in content:
        file.write(c)