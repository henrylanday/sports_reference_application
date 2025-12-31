import json
import pandas as pd

class JsonLoader():
    def __init__(self, json_file_path: str):
        self.JSON_FILE_PATH = json_file_path
        self.json = self.str_to_json(self.load_contents())
    
    def load_contents(self) -> str:
        """
        Loads json file into a str
        
        :return: contents of file at path self.JSON_FILE_PATH otherwise error
        :rtype: str
        """

        try:
            with open(self.JSON_FILE_PATH, 'r') as file:
                return file.read() # Reads the entire file into a string
            # print(content)
        except FileNotFoundError:
            print(f"Error: The file '{self.JSON_FILE_PATH}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def str_to_json(self, file_contents: str) -> json:
        """
        Convert contents of file (type str) into a json item
        
        :param file_contents: contents of file at ./JSON_FILE_PATH
        :type file_contents: str
        :return: json object with the contents of ./JSON_FILE_PATH
        :rtype: json
        """

        try: 
            return json.loads(file_contents)
        except json.JSONDecodeError:
            print("Error loading JSON. Replacing ' single quotes with double per json standard format")
            new_contents = file_contents.replace("\n", "").replace("'", '"')
            return json.loads(new_contents)


class DataFrameBuilder():
    def __init__(self, json: json):
        self.json = json
        self.df: pd.DataFrame = self.json_to_df()
    
    def json_to_df(self) -> pd.DataFrame:
        """
        Convert json into a pandas DataFrame. 
        
        :return: json converted from json into a pandas Dataframe
        :rtype: DataFrame
        """
        try:
            self.df = pd.DataFrame.from_dict(self.json)
            return self.df
        except Exception as e:
            raise ValueError(f"Failed to convert JSON to DataFrame: {e}")
        
    
class BuildSportsReferenceTable(DataFrameBuilder):
    def __init__(self, json):
        super().__init__(json)
        self.table: pd.DataFrame = self.build_table()
    
    def build_table(self) -> pd.DataFrame:
        """
        Build a pretty table showing the number of wins and losses each team has versus each other team in the given DataFrame
        
        Returns
        -------
        pandas.DataFrame
            A square DataFrame where both the index and columns are team abbreviations.
            Each cell contains the number of wins for the row team against the column team.

            The diagonal (team vs itself) contains missing values.

            Example structure:

                    BRO  BSN  CHC  CIN  NYG  PHI  PIT  STL
                BRO   --   10   15   15   14   14   15   11
                BSN   12   --   13   13   13   14   12    9
                CHC    7    9   --   12    7   16    8   10
                CIN    7    9   10   --   13   13   13    8
                NYG    8    9   15    9   --   12   15   13
                PHI    8    8    6    9   10   --   13    8
                PIT    7   10   14    9    7    9   --    6
                STL   11   13   12   14    9   14   16   --
        """

        table = self.df.sort_index().sort_index(axis=1)
        return table.map(lambda x: x['W'] if isinstance(x, dict) else x)

def main(json_file_path: str):
    json_loader = JsonLoader(json_file_path)
    json = json_loader.json
    table_builder = BuildSportsReferenceTable(json)
    table: pd.DataFrame = table_builder.table
    print(table)



if __name__ == "__main__":
    main("./data.json")