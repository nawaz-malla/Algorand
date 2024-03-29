from pyteal import *

router = Router(    "state manipulation",
    BareCallActions(
        no_op=OnCompleteAction.create_only(Approve()),
        opt_in=OnCompleteAction.call_only(Approve()),
        close_out=OnCompleteAction.call_only(Approve()),
        update_application=OnCompleteAction.always(Approve()),
        delete_application=OnCompleteAction.always(Approve()),
    ),
    clear_state=Approve(),
)


### Global State Operations ###
@router.method
def writeGlobal(quote: abi.String):
    return App.globalPut(Bytes("quote"), quote.get())


@router.method
def readGlobal(*, output: abi.String):
    return output.set(App.globalGet(Bytes("quote")))


@router.method
def deleteGlobal():
    return App.globalDel(Bytes("quote"))


### Local State Operations ###


@router.method
def writeLocal(name: abi.String):
    return App.localPut(Txn.sender(), Bytes("name"), name.get())

@router.method
def readLocal(*, output: abi.String):
    return output.set(App.localGet(Txn.sender(), Bytes("name")))


@router.method
def deleteLocal():
    return App.localDel(Txn.sender(), Bytes("name"))

### Create ###

@router.method
def createBox(box_name: abi.String):
    return Assert(App.box_create(box_name.get(), Int(9)))

@router.method
def createBoxWithPut(box_name: abi.String, box_value: abi.String):
    return App.box_put(box_name.get(), box_value.get())

### Write ###

@router.method
def replaceBox(box_name: abi.String, new_name: abi.String):
    return App.box_replace(box_name.get(), Int(0), new_name.get())

@router.method
def writeBox(box_name: abi.String, new_name: abi.String):
    return App.box_put(box_name.get(), new_name.get())

### Read ###

@router.method
def extractBox(box_name: abi.String, start:abi.Uint8, end:abi.Uint8, *, output: abi.String):
    return output.set(App.box_extract(box_name.get(), start.get(), end.get()))

@router.method
def getBox(box_name: abi.String, *, output: abi.String):
    return Seq(
            contents := App.box_get(box_name.get()), # box_get returns a maybeValue with Boolean and box Content.
            Assert(contents.hasValue()),
            output.set(contents.value())
       )   

### delete ###

@router.method
def deleteBox(box_name: abi.String):
    return Assert(App.box_delete(box_name.get()))

### box size ###

@router.method
def getBoxSize(box_name: abi.String, *, output:abi.Uint64):
    return Seq(
            length := App.box_length(box_name.get()), # box_length returns a maybeValue with Boolean and box length.
            Assert(length.hasValue()),
            output.set(length.value())
        )


if __name__ == "__main__":
    
    import os
    import json

    path = os.path.dirname(os.path.abspath(__file__))
    approval, clear, contract = router.compile_program(version=8)
    print("welcome to algorand world")
    print("teal program is generated and stored in artifacts folder")
    # Dump out the contract as json that can be read in by any of the SDKs
    with open(os.path.join(path, "artifacts/contract.json"), "w") as f:
        f.write(json.dumps(contract.dictify(), indent=2))

    # Write out the approval and clear programs
    with open(os.path.join(path, "artifacts/approval.teal"), "w") as f:
        f.write(approval)

    with open(os.path.join(path, "artifacts/clear.teal"), "w") as f:
        f.write(clear)
