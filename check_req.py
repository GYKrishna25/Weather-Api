import pkg_resources

# Read the requirements file
with open('requirements.txt') as f:
    required = f.read().splitlines()

print("Required packages:", required)

# Check each package
installed = {pkg.key for pkg in pkg_resources.working_set}
# print("Installed packages:", installed)

# Identify missing packages
missing = [pkg for pkg in required if pkg.split('==')[0] not in installed]

if missing:
    print("Missing packages:")
    for pkg in missing:
        print(pkg)
else:
    print("All packages in requirements.txt are installed.")