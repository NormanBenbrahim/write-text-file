import numpy as np 
import pandas as pd 
import os 
from sys import argv



class MyApp():

    def create_sample_data(self, data_fname):
        """
        TODO docs
        """

        try:

            # number of rows in the file
            shape = 1000

            hours = np.random.randint(100*9, size=shape)
            accounts = np.array([x+1 for x in range(shape)])

            # sampling from the normal distribution and adding 50 to make
            # it a realistic rate
            rates = 50 + np.random.randn(shape)
            total_cost = hours*rates

            # collect the data
            dataset = pd.DataFrame({"account_number": accounts, "billable_hours": hours, "rate": rates, "total": total_cost})

            # save as file
            dataset.to_csv(data_fname, index=False)

        except Exception as e:
            print("error occured: {}".format(e))

        def 

                                


    #self.create_sample_data()


if __name__ == '__main__':

    # start the app
    app = MyApp()

    # print some output messages
    data_fname = argv[1]

    if os.path.exists(data_fname):
        print("sample file {} already exists, deleting".format(data_fname))
        os.remove(data_fname)
    
    print("creating sample data")
    app.create_sample_data(data_fname)