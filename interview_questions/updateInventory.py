def updateInventory(arr1, arr2):
    label1 = [items[1] for items in arr1]
    label2 = [items[1] for items in arr2]
    for label in label2:
        if label not in label1:
            arr1.append(arr2[label2.index(label)])
        else:
            arr1[label1.index(label)][0] += arr2[label2.index(label)][0]
    print(sorted(arr1, key = lambda x: x[1]))

curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

# updateInventory(curInv, newInv);
updateInventory([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]])