from enum import Enum


class Mood(Enum):
    Joyful = 1
    Grumpy = 2
    Irritated = 3
    Hulk = 4


class MoodCalculator:

    def calculate_mood(self, sleep_deprivation: int, blood_sugar: int) -> Mood:
        """
        Calculate humans Mood based on  and blood sugar
        :param sleep_deprivation: hours since last nap. Must be within 0 and 36 inclusive
        :param blood_sugar: glucose mmol/L. Must be within 70 to 90 inclusive
        :return: mood
        """
        if not 0 <= sleep_deprivation <= 36:
            raise ValueError("Sleep Deprivation: %s not within valid range (%s, %s)" % (sleep_deprivation, 0, 36))

        # student to complete the rest of the function and write the tests

        if not 70 <= blood_sugar <= 90:
            raise ValueError("Blood Sugar: %s not withing valid range (%s, %s)" % (blood_sugar, 70, 90))

        if 0 <= sleep_deprivation <= 26 and 70 <= blood_sugar <= 75:
            return Mood(3).name

        if 0 <= sleep_deprivation <= 26 and 75 < blood_sugar <= 90:
            return Mood(1).name

        if 26 < sleep_deprivation <= 36 and 70 <= blood_sugar <= 75:
            return Mood(2).name

        if 26 <= sleep_deprivation <= 36 and 75 < blood_sugar <= 90:
            return Mood(4).name





