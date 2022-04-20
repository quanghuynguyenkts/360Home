from Autodesk.Revit.DB import Transaction, BuiltInParameterGroup,Category,BuiltInCategory

from pyrevit import forms

uidoc = __revit__.ActiveUIDocument

# Get Document 
doc = uidoc.Document

# Get Application
app = doc.Application

# items = ['item1', 'item2', 'item3']
#result  = forms.SelectFromList.show(items, button_name='Select Item',multiselect = True)

def run():
    file = app.OpenSharedParameterFile()
    if not file:
        return
    myGroups = file.Groups
    dicta={}
    myDefinitions = []
    for a in myGroups:
        dicta[a.Name] = [b.Name for b in a.Definitions]
        for b in a.Definitions:
            myDefinitions.append(b)
        # group = myGroups[a.Name]
        # for b in group.Definitions:
        #     definition = group.Definitions[b.Name]
        #     myDefinitions.append(definition)
        # defName = []
        # for e in myDefinitions:
        #     defName.append(e.Name)

    result  = forms.SelectFromList.show(dicta, button_name='Select Parameters',multiselect = True)
    if not result:
        return
    # result => string

    listSelectedDefinition = []
    

    for b in myDefinitions:
        if b.Name in result:
            listSelectedDefinition.append(b)
    

    categories = doc.Settings.Categories

    myCategories = []
        # for c in categories:
        #     myCategories.Add(c.Name, c)

    for c in categories:
        if c.AllowsBoundParameters:   
            myCategories.append(c.Name)
    sortedCategories = sorted(myCategories)
        
    result2  = forms.SelectFromList.show(sortedCategories, button_name='Select Categories',multiselect = True)
    if not result2:
        return
    selectedCategories = []
        
    for d in categories:
        if d.Name in result2:
            selectedCategories.append(d)

    # categories = []

    # categories.append(Category.GetCategory(doc,BuiltInCategory.OST_ProjectInformation))

    catSet = doc.Application.Create.NewCategorySet()
    for cat in selectedCategories:

            # if cat.AllowsBoundParameters:
        catSet.Insert(cat)

    trans = Transaction(doc, "Create Project Information Parameter")

    trans.Start()
    binding = doc.Application.Create.NewInstanceBinding(catSet)
    for definition in listSelectedDefinition:
        doc.ParameterBindings.Insert(definition, binding, BuiltInParameterGroup.PG_IDENTITY_DATA)
    trans.Commit()

run()






#     print(dicta)
#     # group = myGroups("1_Thong-tin-chung")
#     group = myGroups["0_Thong-tin-chung"]
#     print(group.Definitions)
   
#     definition = group.Definitions["360Home_MaDuAn"]

# categories = []

# categories.append(Category.GetCategory(doc,BuiltInCategory.OST_ProjectInformation))

# catSet = doc.Application.Create.NewCategorySet()
# for cat in categories:

#     if cat.AllowsBoundParameters:
#         catSet.Insert(cat)

# trans = Transaction(doc, "Create Project Information Parameter")

# trans.Start()
# binding = doc.Application.Create.NewInstanceBinding(catSet)
# doc.ParameterBindings.Insert(definition, binding, BuiltInParameterGroup.PG_DATA)
# trans.Commit()