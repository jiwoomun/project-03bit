from crime_cctv.models import CctvDTO
from crime_cctv.services import CctvService

class Controller(object):

    @staticmethod
    def main():
        while 1:
            menu = input('0-Exit 1-서울에 있는 cctv 2-DF생성')
            if menu == '0':
                break
            elif menu == '1':
                cctvinseoul = ()

                CctvService.dto = CctvService.new_model('housing')
                print(dataset.housing)
            else:
                continue


Controller.main()