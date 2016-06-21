# Electronic

## Description
This class represents the electronic tools in the Codecool.

## Parent class
None

## Attributes

* ```name```
  * data type: string
  * description: Name of the electronic tool.
* ```switch```
  * data type: boolean
  * description: Condition of the electronic tool.
  * If is True, then the tool is ON, when False, then OFF
* ```error```
   * data type: boolean
   * description: Efficiency of the electronic tool.
   * It is True, then the toll not working, when False, then usage.

## Class methods

None

#### Arguments
None

#### Return value
```error``` attribute

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```tool_switcher```

Check the error attribute. If False, then switch the switch boolean. If not, then give an error message.

#### Arguments

None

#### Return value
None
