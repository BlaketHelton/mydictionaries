# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''




datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}

import csv

with open('retail_space.csv', 'w') as x:
  w = csv.DictWriter(x, fieldnames=["room-number", "use", "sq-ft", "price"])
  w.writeheader()
  for row in datastore['medical']:
    w.writerow(row)

#or you can use:

# import csv

#retail_space = open("retail_space.csv", "w")
#retail_space.csv = csv.writer(retail_space)

#keys = datastore["medical"][0].keys()
#retail_space_csv.writerow(keys)

#for i in range(len(retail_space))
  #blah blah blah 

#retail_space.close()

#or you can use:

#outfile = open('retail_space.csv','w')
#outfile.write('room-number,use,sq-ft,print\n')

#list = datastore['medical']

#for each in list:
  #rn = each['rrom-number']
  #etc...

  #outfile.write(str(rn) + ',' + use + ',' + str(sq) + ',' + str(price) + '\n')

#outfile.close()