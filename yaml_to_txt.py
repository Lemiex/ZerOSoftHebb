# import yaml

# with open("environment_pytorch==1.7.1.yml") as file_handle:
#     environment_data = yaml.safe_load(file_handle)

# with open("requirements.txt", "w") as file_handle:
#     for dependency in environment_data["dependencies"]:
#         package_name, package_version, _ = dependency.split("=")
#         file_handle.write("{} == {}\n".format(package_name, package_version))

import yaml

data = yaml.safe_load(open('environment_pytorch==1.7.1.yml'))

requirements = []
for dep in data['dependencies']:
    if isinstance(dep, str):
        package, package_version, python_version = dep.split('=')
        if python_version == '0':
            continue
        requirements.append(package + '==' + package_version)
    elif isinstance(dep, dict):
        for preq in dep.get('pip', []):
            requirements.append(preq)

with open('requirements.txt', 'w') as fp:
    for requirement in requirements:
       print(requirement, file=fp)