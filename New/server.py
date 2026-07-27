# ==========================================================
# Election Software - Server
# ----------------------------------------------------------
# Responsibilities:
# - Starts the election server
# - Loads election configuration
# - Loads candidate information
# - Sends election data to clients
# - Receives votes from clients
# - Saves votes
#
# This file DOES NOT:
# - Create the GUI
# - Display pages
# - Handle Tkinter widgets
# ==========================================================


class ElectionServer:
    """
    Handles all server-side operations.
    """

    def __init__(self):
        # -------------------------
        # Connected clients
        # -------------------------
        self.clients = []

        # -------------------------
        # Elections loaded from CSV
        # -------------------------
        self.elections = []

        # -------------------------
        # Votes received
        # -------------------------
        self.votes = []

    # ======================================================
    # Server
    # ======================================================

    def start_server(self):
        """
        Starts the socket server.

        TODO:
        - Open socket
        - Listen for incoming clients
        """
        pass

    # ======================================================
    # Election Data
    # ======================================================

    def load_elections(self):
        """
        Loads all election information.

        TODO:
        - Read elections.csv
        - Read candidate CSV files
        - Create Candidate objects
        """
        pass

    # ======================================================
    # Client Communication
    # ======================================================

    def send_election_data(self, client):
        """
        Sends election data to a connected client.
        """
        pass

    def receive_vote(self, client):
        """
        Receives a completed vote from a client.
        """
        pass

    # ======================================================
    # Results
    # ======================================================

    def save_vote(self, vote):
        """
        Saves a vote to the results.
        """
        self.votes.append(vote)