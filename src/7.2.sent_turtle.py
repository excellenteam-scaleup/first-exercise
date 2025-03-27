class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        try:
            user_box = self.boxes[recipient]
        except KeyError:
            print("Recipient does not exist.")
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': title,  # added title (obvious)
            'body': message_body,
            'sender': sender,
            'unread': True  # added read/unread status
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username=None, N=None):
        messages = []
        if username not in self.boxes or username == None or N == None:
            return [message for message_list in self.boxes.values() for message in
                    message_list]  # doesn't change unread status
        if len(self.boxes[username]) >= N:
            N = len(self.boxes[username])
        for message_index in range(N):
            if (N < len(self.boxes[username])): N = len(self.boxes[username])
            if self.boxes[username][message_index]['unread'] == True:
                self.boxes[username][message_index]['unread'] = False
                messages.append(self.boxes[username][message_index])
        return messages

    def search_inbox(self, username, substr):
        return [message for message in self.boxes[username] if
                message['title'].find(substr) != -1 or message['body'].find(substr) != -1]


def main():
    # Code here:
    ""


if __name__ == "__main__":
    main()
