import c_and_a as c


class Kinds:
    def __init__(self):
        self.royal_flush = 4
        self.straight_flush = 10 * 4 - self.royal_flush
        self.four_of_a_kind = 13 * 4 * 12
        self.full_house = 13 * c.c(4, 3) * 12 * c.c(4, 2)
        self.flush = 4 * c.c(13, 5) - self.straight_flush - self.royal_flush
        self.straight = 10 * 4**5 - self.straight_flush - self.royal_flush
        self.three_of_a_kind = int(13 * c.c(4, 3) * 12 * 4 * 11 * 4 / c.a(2, 2))
        self.two_pair = int(13 * c.c(4, 2) * 12 * c.c(4, 2) * 11 * 4 / c.a(2, 2))
        self.pair = int(13 * c.c(4, 2) * 12 * 4 * 11 * 4 * 10 * 4 / c.a(3, 3))
        self.high_card = (
            c.c(52, 5)
            - 10 * 4**5
            - self.four_of_a_kind
            - self.full_house
            - self.flush
            - self.three_of_a_kind
            - self.two_pair
            - self.pair
        )


k = Kinds()
print(
    k.royal_flush,
    k.straight_flush,
    k.four_of_a_kind,
    k.full_house,
    k.flush,
    k.straight,
    k.three_of_a_kind,
    k.two_pair,
    k.pair,
    k.high_card,
)
