original_bill=0
total_bill=0
tip_percentage=.18
tip = 0
number_of_people=1
bill_per_person=0

def calculate_bill():
    global tip
    tip = original_bill * tip_percentage

    global total_bill
    total_bill = original_bill + tip

    if number_of_people > 1:
        global bill_per_person
        bill_per_person = total_bill / number_of_people


def prompt_user():
    global original_bill
    original_bill = float(raw_input('How much is the bill not including tip?'))

    dine_alone = raw_input('Did you dine alone? Y or N')
    if dine_alone == 'N':
        global number_of_people
        number_of_people = int(raw_input('How many people were at dinner?'))
    
    standard_tip = raw_input('Is 18% tip okay? Y or N')
    if standard_tip == 'N':
        global tip_percentage
        tip_percentage = float(raw_input('How much do you want to leave for tip?'))


def display_bill_amount():
    print 'original bill is', original_bill
    print 'tip amount is', tip
    print 'total_bill is', total_bill
    
    if number_of_people > 1:
        print 'each person pays', bill_per_person


def main():
    prompt_user()
    calculate_bill()
    display_bill_amount()

if __name__ == '__main__':
    main()
