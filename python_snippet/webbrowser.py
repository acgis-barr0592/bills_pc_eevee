def main():
    searchName()

def searchName():
    '''this function takes a given name adds a random last name and searches duckduckgo with the full name
    needs webbrowser and names module'''

    import webbrowser
    reload(webbrowser)


    firstName = raw_input("enter first name here")
    lastName = "blank"


    try:
        import names
        global namesImport
        namesImport = 1
    except:
        webbrowser.open("https://pypi.org/project/names/", new=2, autoraise=True)
        namesImport = 0
        exceptError = "this didnt work! install names with pip install names"
        print exceptError
        sys.exit()

    finally:
        if namesImport == 1:
            lastName = names.get_last_name()
            fullName = firstName + "+" + lastName
        if namesImport == 0:
            print "something broke!"


    basePageName = "duckduckgo.com/?q="
    pageName = basePageName + fullName
    webbrowser.open(pageName, new=2, autoraise=True)

if __name__ == '__main__':
    main()



