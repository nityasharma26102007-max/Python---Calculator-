exp =[
    {
    "experiment ":"exp1",
    "reading ":(10,20,20,30),
    "status ":{"valid"}
    },
    {
        "experiment ":"exp2",
        "reading ":(5,5,10),
        "status ":{"outerlier","retry"}
        },
        {
            "experiment ":"exp3",
            "reading ":(40,50,50,60),
            "status":{"valid","retry"}
            }
    ]
print("updated readings:")
for e in exp:
    exp[0]["reading "]=tuple(dict.fromkeys(exp[0]["reading "]))
    exp[1]["reading "]=tuple(dict.fromkeys(exp[1]["reading "]))
    exp[2]["reading "]=tuple(dict.fromkeys(exp[2]["reading "]))
    
print("exp1 : ",exp[0]["reading "])
print("exp2 : ",exp[1]["reading "])
print("exp3 : ",exp[2]["reading "])

print("Outlier Experiment:")
print(list(exp[1]["status"].value))
    