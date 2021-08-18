cmake_minimum_required(VERSION 3.4...3.18)


add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/UploadPypi.txt
  COMMAND python3.8 -m twine upload --password ${Password} --username ${Token} --repository pypi ./dist/*
  COMMENT Upload on Pypi $)

add_custom_target(UploadPypi ALL DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/UploadPypi.txt)
