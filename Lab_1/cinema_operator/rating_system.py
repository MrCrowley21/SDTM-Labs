# class for defining the rating system
class RatingSystem:
    # append the new rating of a cinematographic object to the rating list
    def give_rating(self, cinema):
        print(f'Rate the {cinema.get_title()}, using an integer from 1 to 5')
        try:
            user_rating = int(input())
        except:
            raise Exception('Use rating should be an integer between 1 and 5')
        cinema.rating_list.append(user_rating)

    # compute the current rating list
    def modify_general_rating(self, cinema):
        rating_sum = 0
        for i in cinema.rating_list:
            rating_sum += i
        cinema.rating = rating_sum / len(cinema.rating_list)
