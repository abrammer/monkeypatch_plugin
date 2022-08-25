## Experiments with monkeypatching

This is just a quick dumb repo to investigate monkeypatching methods from an external (child) module onto a parent module. 

This utilises a simple decorator that will monkey patch various child methods onto parent module when the child module is imported.  

Using a config in the parent, the external module is defined, imported and the child class is available. 

## installation
To add a custom reader into the module use the decorator `pipeliner.utils.register_reader`.  To make your decorator globally visible to `pipeliner` the addon must be installed into the environment with `pipeliner` somewhere in the module name.  e.g. `pipeliner_xyzreader` or `xyzreader_pipeliner`. 
This is not needed for interactive sessions or any code which would import the addon manually.  

## pipeliner config
An example of defining functions and readers outside of code is container in `pipeliner.main` and `pipeliner/config.yaml`.
Running `pipeliner/main.py` will execute both the container pipeliner reader and the custom_addon reader.  