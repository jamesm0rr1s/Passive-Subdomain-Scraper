# Requirements
# pip install beautifulsoup4
# pip install colorama

import csv # For creating the list of subdomains
import pip # For installing requirements
import sys # For terminating the script with a status code from main
import urllib2 # For getting the web page contents



# Check if being run from IDLE
def check_idle():

    # Check if being run from IDLE
    if ("idlelib" in sys.modules):

        # Tell the user to run from the command line
        print("Run from the command line: \"python SubScrape.py\"")

        # exit
        sys.exit()



# Check if being run from IDLE
check_idle()



# Check if requirements are installed
package = "colorama"

# Try to import the package
try:

    # Import Colorama
    from colorama import Fore, Back, Style
    import colorama

# Package not installed
except:

    # Check if pip has the attribute main
    if hasattr(pip, 'main'):

        # Install the package
        pip.main(['install', package])

    # Pip does not have the attribute main
    else:

        # Install the package
        pip._internal.main(['install', package])

    # Try to import after the install
    try:

        # Import Colorama
        from colorama import Fore, Back, Style
        import colorama

    # Package was not installed
    except:

        # Tell the user the command to run to install manually
        print("Unable to install " + package + ". Run \"pip install " + package + "\"")

# Initialize colorama
colorama.init()



# Check if requirements are installed
package = "beautifulsoup4"

# Try to import the package
try:
        
    # Import BeautifulSoup parsing the web page contents
    from bs4 import BeautifulSoup

# Package not installed
except:

    # Check if pip has the attribute main
    if hasattr(pip, 'main'):

        # Install the package
        pip.main(['install', package])

    # Pip does not have the attribute main
    else:

        # Install the package
        pip._internal.main(['install', package])

    # Try to import after the install
    try:

        # Import BeautifulSoup
        from bs4 import BeautifulSoup

    # Package was not installed
    except:

        # Tell the user the command to run to install manually
        print("Unable to install " + package + ". Run \"pip install " + package + "\"")



# Set the colors
bo = Style.BRIGHT
gr = bo + Fore.GREEN
bl = bo + Fore.BLUE
ye = bo + Fore.YELLOW
re = bo + Fore.RED
cb = bo + Fore.CYAN
wh = Fore.WHITE
en = Style.RESET_ALL

# Set the statuses
success = bo + gr + "[+] " + Style.RESET_ALL
info    = bo + bl + "[*] " + Style.RESET_ALL
warning = bo + ye + "[-] " + Style.RESET_ALL
failure = bo + re + "[!] " + Style.RESET_ALL

# Print the banner
def print_banner():

    # Print the title
    print(gr)
    print(" ██████╗██╗  ██╗█████╗   ██████╗ █████╗█████╗  ████╗ █████╗ ██████╗ ".decode('utf8'))
    print(" ██╔═══╝██║  ██║██╔═██╗  ██╔═══╝██╔═══╝██╔═██╗██╔═██╗██╔═██╗██╔═══╝ ".decode('utf8'))
    print(" ██████╗██║  ██║█████╔╝  ██████╗██║    █████╔╝██████║█████╔╝████╗   ".decode('utf8'))
    print(" ╚═══██║██║  ██║██╔═██╗  ╚═══██║██║    ██╔═██╗██╔═██║██╔══╝ ██╔═╝   ".decode('utf8'))
    print(" ██████║╚█████╔╝█████╔╝  ██████║╚█████╗██║ ██║██║ ██║██║    ██████╗ ".decode('utf8'))
    print(" ╚═════╝ ╚════╝ ╚════╝   ╚═════╝ ╚════╝╚═╝ ╚═╝╚═╝ ╚═╝╚═╝    ╚═════╝ ".decode('utf8'))
    print(en)
        
    # Set the offset
    offset = " " * 13

    # Set the details with 42 spaces
    line00 = "                                          "
    line01 = "                SubScrape                 "
    line02 = "                                          "
    line03 = "        Passive Subdomain Scraper         "
    line04 = "               Version: 1.0               "
    line05 = "                                          "
    line06 = "         Created by: James Morris         "
    line07 = "                                          "
    line08 = "      Visit: github.com/jamesm0rr1s       "
    line09 = "    Follow me on Twitter: @jamesm0rr1s    "
    line10 = "  Connect on linkedin.com/in/jamesm0rr1s  "
    line11 = "                                          "

    # Print the details
    print(offset + line00)
    print(offset + gr + line01 + en)
    print(offset + line02)
    print(offset + wh + line03[:15] + en + gr + line03[15:19] + en + wh + line03[19:26] + en + gr + line03[26:32] + en + wh + line03[32:] + en)
    print(offset + wh + line04[:24] + en + wh + line04[24:] + en)
    print(offset + line05)
    print(offset + wh + line06[:21] + en + cb + line06[21:] + en)
    print(offset + line07)
    print(offset + wh + line08[:12] + en + gr + line08[12:] + en)
    print(offset + wh + line09[:25] + en + cb + line09[25:] + en)
    print(offset + wh + line10[:12] + en + gr + line10[12:] + en)
    print(offset + line11)



# Open the URL and return the BeautifulSoup
def get_soup(url):

    # Try to open the url
    try:
        # Open the url
        response = urllib2.urlopen(url)

    # Catch exceptions
    except urllib2.URLError as e:

        # Tell the user that there was an error
        print(failure + "An error occured fetching " + url + " \n " + e.reason + "\n")

        # Return there was an error
        return "Error"

    # Return the soup
    return BeautifulSoup(response.read(), "html.parser")



# Ask the user for the domain
def ask_user_for_domain():

    # Set a blank error message
    errorMessage = ""

    # Loop until a valid domain has been entered
    while True:

        # Ask the user to enter a domain
        domain = raw_input("\n" + errorMessage + "Enter the domain to search for such as \"example.com\"" + "\n").lower()

        # Check if an incorrect domain was entered
        if "." not in domain:

            # Set the error message to incorrect domain entered
            errorMessage = failure + "Incorrect domain entered. "

        # Correct domain entered
        else:

            # Return the domain
            return domain



# Ask the user for the output filename
def ask_user_for_output_filename(domain):

    # Ask the user for the output filename
    outputFilename = raw_input("\n" + "Enter a filename for the output. (subdomains-" + domain + ".csv)" + "\n")

    # Check if no name was given
    if outputFilename == "":

        # Set the file name
        outputFilename = "subdomains-" + domain + ".csv"

    # A name was given
    else:

        # Print a blank line
        print("")

    # Check if a valid file extension was added by the user
    if outputFilename[-4:] != ".csv":

        # Add the file extension
        outputFilename = outputFilename + ".csv"

    # Tell the user the filename
    print(info + "The list of subdomains will be saved as " + outputFilename + "\n")

    # Return the filename
    return outputFilename



# Parse the subdomains
def parse_soup(soup, domainToSearchFor, listOfSubdomains):

    # Try to parse the soup
    try:

        # Loop through all of the "div" tags with a class of "domains"
        for div in soup.findAll("div", {"class": "domains"}):

            # Remove "http://"
            subdomain = div.text.strip().strip().replace("http://", "")

            # Check if the main domain is in the subdomain
            if domainToSearchFor in subdomain:

                # Check if the subdomain is not in the list
                if [subdomain] not in listOfSubdomains:

                    # Append the subdomain to the list
                    listOfSubdomains.append([subdomain])

                    # Print the subdomain
                    print(success + subdomain)

    # Unable to parse the soup
    except:

        pass



# Save the list of subdomains
def save_subdomains(filename, domainToSearchFor, listOfSubdomains):

    # Check that there are subdomains to save
    if len(listOfSubdomains) > 1:

        # Save the results as a csv file
        with open(filename, "wb") as fileOfSubdomains:
            csvWriter = csv.writer(fileOfSubdomains)
            csvWriter.writerows(listOfSubdomains)

        # Tell the user the file has been saved
        print("\n" + info + "Results have been saved to " + filename)

    # No subdomains found
    else:

        # Tell the user that there were no matches
        print(warning + "No matches found for \"" + domainToSearchFor + "\"")



# Main
def main():

    # Print the banner
    print_banner()
    
    # Create a list with a column header to store the subdomains
    listOfSubdomains = []
    listOfSubdomains.append(["Subdomains"])

    # Ask the user for the domain to search for
    domainToSearchFor = ask_user_for_domain()

    # Ask the user for the output filename
    outputFilename = ask_user_for_output_filename(domainToSearchFor)

    # Get the subdomains
    soup = get_soup("https://findsubdomains.com/subdomains-of/" + domainToSearchFor)

    # Parse the subdomains
    parse_soup(soup, domainToSearchFor, listOfSubdomains)

    # Save the list of subdomains
    save_subdomains(outputFilename, domainToSearchFor, listOfSubdomains)



# Only execute when running as primary module or called from another script
if __name__ == "__main__":

    # Execute main, get status code
    status = main()

    # Terminate with status code from main
    sys.exit(status)
