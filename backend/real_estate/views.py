from real_estate.housing import Housing
from real_estate.dataset import Dataset

class Controller(object):

    @staticmethod
    def main():
        while 1:
            menu = input('0-Exit 1-모델생성 2-DF생성')
            if menu == '0':
                break
            elif menu == '1':
                housing = Housing()
                dataset = Dataset()
                dataset.housing = housing.new_model('housing')
                print(dataset.housing)
            else:
                continue


    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. Housing 의 type 은 \n {type(this.train)} 이다.')
        print(f'2. Housing 의 column 은 \n {this.train.columns} 이다.')
        print(f'3. Housing 의 상위 5개 행 \n {this.train.head(5)} 이다.')
        print(f'4. Housing 의 null의 갯수 \n {this.train.isnull().sum()}개')

        print('*' * 100)

Controller.main()