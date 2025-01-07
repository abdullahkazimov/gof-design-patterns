from observer import StandardSubscriber, PremiumSubscriber, NetflixStream

stream = NetflixStream()

user1 = StandardSubscriber()
user2 = PremiumSubscriber()

stream.add_subscriber(user1)
stream.add_subscriber(user2)

stream.notify_subscribers()

stream.remove_subscriber(user2)

stream.notify_subscribers()