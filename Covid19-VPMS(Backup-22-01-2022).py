# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:12:38 2021

@author: APARNA
"""

# COVID 19 Vaccination Progress Management System(VPMS)
# Last Updated: 22 Jan 2022

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import click
import sys
from datetime import date
from datetime import datetime


# Load Master Data file and Datasets
click.clear()
MasterDataFileName = 'country_vaccinations.csv'
VaccineBrandFileName = "VacVsCountries.csv"
CountriesFileName = "Countries.csv"
MonthlyVacIndiaFileName="Monthly vaccinations.csv"

# ---------------------------------------------------

# -------Function to Plot Pie Chart from VacVsCountries Dataset
def PlotChart3(FileName):
    

    # Read Data from Filename(Csv file) and Plot Pie chart of Brand Vs Countries
    
    DFOriginalVax=pd.read_csv(FileName,sep=',',header=0,index_col='Vaccine')
    DFOriginalVax.plot(kind='pie',y='Countries',legend=False,autopct='%1.0f%%',ylabel='',
                       title="Vaccinations Vs Countries",shadow=True)
   
    plt.show()
# ---------------------------------------------------

# -------Function to Predict Daily Vaccination Rate from Master Data File
# --------------------------------------------------
def Predict_Daily_Vaccine_Rate(FileName):
    IndiaPopulation = 1393409033
    # Get Target Population Percentage and Target Date for prediction
    TargetPopulationPercentage = int(input("    Enter target population percentage to be vaccinated ONCE: "))

    # Get Last date of Master Data and Daily Vaccination

    TargetVaccinationDate = input("    Enter the date by which the vaccination target is to be met (dd-mm-yy): ")
    # ----------------------------------------------------------------
    # Read Data from master file
    DFOriginalVax = pd.read_csv(FileName, sep=',', header=0)
    CountryFilter = (DFOriginalVax["country"] == "India")
    DFNew = DFOriginalVax[CountryFilter].filter(
        ["country", "date", "people_vaccinated", "people_fully_vaccinated"]).tail(2)
    LastDate = DFNew.iat[1, 1]
    DailyVaccinations = int(DFNew.iat[1, 2]-DFNew.iat[0, 2])
    Vaccinated = DFNew.iat[1, 2]

    #   Calculate Number of Days
    Start = datetime.strptime(LastDate, '%d-%m-%Y').date()
    End = datetime.strptime(TargetVaccinationDate, '%d-%m-%Y').date()

    NumberOfDays = (End-Start).days

    #   Calculate Predicted daily Vaccination Rate and Print
    PopulationToBeVaccinated= IndiaPopulation * \
        (TargetPopulationPercentage)/100-Vaccinated
    PredictedDailyVacRate = int(PopulationToBeVaccinated/NumberOfDays)
    print("_"*70, "\n")
    print("\n    Current Rate of Daily Vaccinations: ",DailyVaccinations)
    print("\n    Predicted Daily Vaccine Rate to reach Target in ",NumberOfDays, "days:", PredictedDailyVacRate)
    print("_"*70, "\n")
    
    INPUT = input("    Press any key to continue: ")

# ----------End Function-Predict_Daily_Vaccine_Rate---------------

# -------Function to Predict No of Days from Master Data File
# ----------------------------------------------------------------
def Predict_No_Of_Days(FileName):
    IndiaPopulation = 1393409033
    # Get Target Population Percentage and Target Date for prediction
    TargetPopulationPercentage = int(input(
        "    Enter target population percentage to be vaccinated AT CURRENT RATE:"))

    # Read Data from master file
    DFOriginalVax = pd.read_csv(FileName, sep=',', header=0)
    CountryFilter = (DFOriginalVax["country"] == "India")
    DFNew = DFOriginalVax[CountryFilter].filter(
        ["country", "date", "people_vaccinated", "people_fully_vaccinated"]).tail(2)

    # Get Last date of Master Data and Daily Vaccination

    LastDate = DFNew.iat[1, 1]
    DailyVaccinations = int(DFNew.iat[1, 2]-DFNew.iat[0, 2])
    Vaccinated = DFNew.iat[1, 2]
    #   Calculate Predicted No of Days and Print
    PopulationToBeVaccinated = IndiaPopulation *(TargetPopulationPercentage)/100-Vaccinated

    PredictedNoOfDays = int(PopulationToBeVaccinated/DailyVaccinations)
    print("_"*70, "\n")
    print("\n    Predicted Days to reach ", TargetPopulationPercentage,
          "% Population Target : ", PredictedNoOfDays)
    print("_"*70, "\n")
    INPUT = input("    Press any key to continue: ")
# -------------End Function - Predict_No_Of_Days------------------


# ------START OF MAIN PROGRAM-------------------------------------
DFVaxFull = pd.read_csv(MasterDataFileName)

#  Display Main Menu

while True:
    
    print("_"*70, "\n")
    print("       WELCOME TO THE VACCINATION PROGRESS MANAGEMENT SYSTEM    ")
    print("_"*70, "\n")
    print("    1. View Vaccination Datasets\n   ")
    print("    2. Enter Vaccination Data (Analyst)\n")
    print("    3. Enter Vaccination Data (User)\n")
    print("    4. View Graphical Visualisation\n")
    print("    5. Predictive Analysis\n")
    print("    6. Export Data\n")
    print("    7. Exit\n")
    print("_"*70, "\n")
    MainMUserCh = int(input("        Enter your choice(1-7):"))

    if MainMUserCh == 1:

        while True:
            #  Display Sub Menu 1 for Viewing Vaccination datasets
            print("_"*80, "\n")
            print("              VIEW VACCINATION DATASETS    ")
            print("_"*80, "\n")
            print('    1. Complete Dataset\n')
            print('    2. Data Set: Monthly Vaccinations in India\n')
            print('    3. Data Set: Total number of vaccinated people across different countries\n')
            print('    4. Data Set: Number of Countries Using different Vaccine Brands\n')
            print('    5. Exit and go back to the Main Menu\n')
            print("_"*80, "\n")
            DataSetUserCh = int(input("Enter your choice(1-5):"))
            # Read the Data Set  CSV File and Print Datasets based on the choice entered
            if DataSetUserCh == 1:
                print("_"*70, "\n")
                print("\n              Vaccination Dataset(up to 20th December 2021)\n")
                print("_"*70, "\n")
                DFVaxFull = pd.read_csv(MasterDataFileName, sep=",", header=0)
                print(DFVaxFull)
                Input=input("Press any key to continue: ")
            elif DataSetUserCh == 2:
                print("_"*70, "\n")
                print("\n             Monthly Vaccinations in India\n")
                print("_"*70, "\n")
                dfMonthlyVac = pd.read_csv('Monthly vaccinations.csv', sep=",", header=0)
                print(dfMonthlyVac)
                Input=input("Press any key to continue: ")
            elif DataSetUserCh == 3:
                print("_"*70, "\n")
                print("\n     Total number of vaccinated people across different countries\n")
                print("_"*70, "\n")
                dfCountries = pd.read_csv('Countries.csv', sep=",", header=0)
                print(dfCountries)
                Input=input("Press any key to continue: ")
            elif DataSetUserCh == 4:
                print("_"*70, "\n")
                print("\n     Number of Countries Using Vaccine Brands\n")
                print("_"*70, "\n")
                dfVacBrandCountries = pd.read_csv(VaccineBrandFileName , sep=",", header=0)
                print(dfVacBrandCountries)
                Input=input("Press any key to continue: ")
            elif DataSetUserCh == 5:
                # Exit the Sub Menu and Go to Main Menu
                break
            else:
                # If invalid Menu choice entered,prompt the user and go back to the menu options
                print("Invalid choice entered.Select the correct Option")

    elif MainMUserCh == 2:
        #  Display Screen for Data Entry by Analyst
        print("_"*70, "\n")
        print("                  DAILY VACCINATION DATA(ANALYST SCREEN)")
        print("_"*70, "\n")
        print("Enter countrywise vaccination records:\n")
        while True:
            #  Read User Input from Analyst ( all fields as in MasterDataFile)
            print("_"*70, "\n")
            LstUserFields = list()
            Country = input("  Enter country name:")
            LstUserFields.append(Country)

            Iso_Code = input("  Enter ISO Code:")
            LstUserFields.append(Iso_Code)

            Date = input("  Enter the date:")
            LstUserFields.append(Date)

            TotalVax = input("  Enter the total vaccinations:")
            LstUserFields.append(TotalVax)

            PeopleVaccinated = int(input("  Enter the number of people vaccinated:"))
            LstUserFields.append(PeopleVaccinated)

            People_fully_vaccinated = int(input("  Enter the number of people fully vaccinated:"))
            LstUserFields.append(People_fully_vaccinated)

            Daily_vaccinations_raw = int(input("  Enter the number of daily vaccinations(RAW):"))
            LstUserFields.append(Daily_vaccinations_raw)

            Daily_vaccinations = int(input("  Enter the number of daily vaccinations:"))
            LstUserFields.append(Daily_vaccinations)

            total_vaccinations_per_hundred = float(input("  Enter the number of total vaccinations per hundred:"))
            LstUserFields.append(total_vaccinations_per_hundred)

            people_vaccinated_per_hundred = float(input("  Enter the number of people vaccinated per hundred:"))
            LstUserFields.append(people_vaccinated_per_hundred)

            people_fully_vaccinated_per_hundred = float(input("  Enter the number of people fully vaccinated per hundred:"))
            LstUserFields.append(people_fully_vaccinated_per_hundred)

            Daily_vaccinations_per_million = int(input("  Enter the number of daily vaccinations per million:"))
            LstUserFields.append(Daily_vaccinations_per_million)

            Vaccines = input("  Enter the vaccines:")
            LstUserFields.append(Vaccines)
            # Convert List to DataFrame
            DFUserFields = pd.DataFrame(LstUserFields)
            # Transpose DataFrame
            DFUserFields_1 = DFUserFields.T

           #  Write Data to file and continue or exit without saving data
            VaxUserChoice = input("Enter S to save and Exit Screen, A to abort, C to save and continue.")
            
            if VaxUserChoice == 'S':
                DFUserFields_1.to_csv(
                    MasterDataFileName, mode='a', index=False, header=False)
                # Exit the Sub Menu and Go to Main Menu
                break
            elif VaxUserChoice == 'A':
                # Exit the Sub Menu and Go to Main Menu
                break
            elif VaxUserChoice == 'C':
                # Write Data to file and continue with Next entry
                DFUserFields_1.to_csv(
                    MasterDataFileName, mode='a', index=False, header=False)
            else:
                # If invalid Menu choice entered,prompt the user and go back to the menu options
                print("Invalid choice entered.Select the correct Option")

    elif MainMUserCh == 3:
         #  Display Screen for Data Entry by Users
         while True:
            print("_"*70, "\n")
            print('                  DAILY VACCINATION DATA(USER SCREEN)')
            print("_"*70, "\n")
            No_of_entries = int(input('Number of entries to be filled:'))
            Name = []
            Age = []
            Vaccination_Status = []
            for i in range(No_of_entries):
               Nm = input('Enter your name: ')
               Ag = int(input('Enter your age: '))
               
               while True:
                   print('\n Vaccination Status: \n')
                   print('1. Not vaccinated ')
                   print('2. Vaccinated once (First dose complete)')
                   print('3. Vaccinated twice (Second dose complete)')
                       
                   Vs = int(input('Enter choice as 1,2,3:'))
                   if(Vs<1 or Vs>3): 
                      print('\nError: Enter a valid input 1,2 or 3')
                   else:   
                      Name.append(Nm)
                      Age.append(Ag)
                      Vaccination_Status.append(Vs)
                      break
            # Create DataFrame to Save the entered data
            User_Analysis_Data = {'Name': Name, 'Age': Age,'Vaccination_Status': Vaccination_Status}
            User_Analysis_DF = pd.DataFrame(User_Analysis_Data)
            
            # Append the DataFrame to CSV File (mode = a)
            User_Analysis_DF.to_csv('UserDataFile.csv', mode='a', index=False, header=False)
            # Read from CSV File to DataFrame and Print the Dataframe
            User_Analysis_DFPermanent = pd.read_csv('UserDataFile.csv')
            print(User_Analysis_DFPermanent)
            
            #Plot the user data in the DataFrame as a Pie Chart using groupby function
            User_Analysis_DFPermanent.groupby(['Vaccination_Status']).count().plot(kind='pie', y='Name', figsize=(
                    5, 5), autopct='%1.0f%%', title=' Vaccination Status', labels=['Never', 'Once', 'Twice'], ylabel='')
            plt.show()  
            # Exit the Sub Menu and Go to Main Menu
            break
    elif MainMUserCh == 4:
            #  Display Sub Menu 4 for Viewing Graphs
        while True:
            print("_"*70, "\n")
            print("            VIEW GRAPHICAL DATA VISUALISATIONS ")
            print("_"*70, "\n")
            print("       1. Comparing Vaccination Progress Across Major Countries-First and Second Dose\n")
            print("       2. Trend of Monthly Vaccination in India\n")
            print("       3. Use of Major Vaccine Brands across Countries\n")
            print("       4. Exit and Go Back to the Main Menu")

            print("_"*70, "\n")
            GraphMUserCh = int(input("         Enter your choice(1-4):"))

            if GraphMUserCh == 1:

                # Read data from CSV File to Dataframe and plot a bar graph with column Country as x axis
                dfCountries=pd.read_csv('Countries.csv',sep=",",header=0)
                dfCountries.plot(kind='bar',x='Country',title='Vaccination progress - by Countries')
                
                # set title and set ylabel
                plt.ylabel('Number of people vaccinated(in billions)')
                plt.show()
                
            elif GraphMUserCh == 2:
                # Read Data from CSV File to dataframe and plot a line Graph with Month as x axis
                   
                dfMonthlyVac=pd.read_csv('Monthly vaccinations.csv',sep=",",header=0)
                dfMonthlyVac.index=['January','February','March','April','May','June','July',
                                    'August','September','October','November','December']
                dfMonthlyVac.plot(kind='line',color=['red','blue'],marker='d')
                
                # set title and set labels and rotation of labels
                plt.title('Monthly Vaccinations-India   ')
                plt.xlabel('Months')
                plt.ylabel('Number of people (in crores)')
                plt.xticks(rotation = 45)
                plt.show()

               
            elif GraphMUserCh == 3:
                # Call the function to Plot the Vaccines Vs Countries data as a Pie Chart
                PlotChart3(VaccineBrandFileName)
                
          
            elif GraphMUserCh == 4:
                # Exit the Sub Menu and Go to Main Menu
                break
            else:
                # If invalid Menu choice entered,prompt the user and go back to the menu options
                print("Invalid choice entered.Select the correct Option")

    elif MainMUserCh == 5:
        # Display Sub Menu 5 for Predictive Analysis
        while True:
            print("_"*70, "\n")
            print("        VIEW PREDICTIVE ANALYSIS")
            print("_"*70, "\n")
            print("1. Predict DAILY VACCINATION RATE (Given Target Population Percentage and Target date)\n")
            print("2. Predict NUMBER OF DAYS for reaching a Target Population Percentage of Vaccination\n")
            print("3. Exit and go back to the Main Menu.\n")
            print("_"*70, "\n")
            AnalysisMUserCh = int(input("Enter your choice(1-3):"))
            
            if AnalysisMUserCh == 1:
                # Call function for Calculating the Predicted Daily Vaccination rate
                Predict_Daily_Vaccine_Rate(MasterDataFileName)
            elif AnalysisMUserCh == 2:
                # Call function for Calculating the Predicted No of Days
                Predict_No_Of_Days(MasterDataFileName)

            elif AnalysisMUserCh == 3:
                # Exit the Sub Menu and Go to Main Menu
                break

            else:
                # If invalid Menu choice entered,prompt the user and go back to the menu options
                print("Invalid choice entered.Select the correct Option")

    elif MainMUserCh == 6:   
        # Export DataFrames as per user's choice for back-up
        while True:
            print("_"*70, "\n")
            print("     EXPORT VACCINATION DATA TO OTHER FILES ")
            
            print("_"*70, "\n")
            print("1. CSV File\n")
            print("2. Excel File\n")
            print("3. Exit and Go Back to the Main Menu.")

            ExportMUserCh = int(input("Enter your choice(1-3):"))

            if ExportMUserCh == 1:  # CSV File
                CSVFileAd = input("Enter the valid path and name of the CSV File (xxx.csv):")
               
                # Check that the file extension is correct
                if CSVFileAd.endswith('.csv'):
                    print("Please wait..this may take a while: ")
                    DFVaxFull.to_csv(path_or_buf=CSVFileAd, sep=',')
                    print("Data written successfully to .CSV File")
                    Input=input("Press any key to continue: ")
                else:
                    print("Invalid extension.Enter file name with .csv extension.")
            elif ExportMUserCh == 2:  # Excel File
                ExcelFileAd = input("Enter the valid path and name of the Excel File(xxx.xlsx):")
                # Check that the file extension is correct               
                if ExcelFileAd.endswith('.xlsx'):
                    print("Please wait..this may take a while: ")
                    DFVaxFull.to_excel(ExcelFileAd)
                    print("Data written successfully to .xlsx File")
                    Input=input("Press any key to continue: ")
                else:
                   print("Invalid extension.Enter file name with .xlsx extension.") 

            elif ExportMUserCh == 3:
                # Exit the Sub Menu and Go to Main Menu
                break
            else:
                # If invalid Menu choice entered,prompt the user and go back to the menu options
                print("Invalid choice entered.Select the correct Option")

    elif MainMUserCh == 7:
         # Exit the Main Menu and Quit from the Program
        print("\n   Thank you for using the VPMS Program\n ")
        Input=input("   Press any key to Exit: ")
        sys.exit()
    else:
        # If invalid Menu choice entered,prompt the user and go back to the menu options
        print("Invalid choice entered.Select the correct Option")
        
# ------END OF MAIN PROGRAM-------------------------------------