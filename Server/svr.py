import socket
import csv
from collections import defaultdict

class VoteServer:
    def __init__(self, host='0.0.0.0', port=65432):
        self.host = host
        self.port = port
        self.positions = [
            "CAPTAIN BOYS",
            "CAPTAIN GIRLS", 
            "VICE CAPTAIN BOYS",
            "VICE CAPTAIN GIRLS" #Posts
        ]
        self.candidates = {
            "CAPTAIN BOYS": ["Praneel Deshmukh", "Abhichandra Charke", "Aadityaraje Desai", "Rachit Srivastav"],
            "CAPTAIN GIRLS": ["Gauravi Zade", "Naisha Rastogi", "Trisha Shah", "Kirthika Jaychander"],
            "VICE CAPTAIN BOYS": ["Sagnik Ghosh", "Kausar Chandra", "Avaneesh Mahalle", "Viren Jadhav", "Krishna Yadav"],  
            "VICE CAPTAIN GIRLS": ["Sumedha Vaidya", "Trisha Kandpal", "Ketaki Phalle", "Riya Shirode", "Kavya Mehta"]   #Candidate's Names 
        }

    def initialize_votes(self):
        """Initialize vote counts to zero for all candidates"""
        return {pos: defaultdict(int) for pos in self.positions}

    def read_existing_votes(self):
        """Read existing votes from CSV file"""
        votes = self.initialize_votes()
        try:
            with open('votes.csv', 'r') as f:
                reader = csv.reader(f)
                current_position = None
                
                for row in reader:
                    if len(row) == 0:
                        continue
                    if row[0] in self.positions:
                        current_position = row[0]
                    elif current_position and len(row) >= 2:
                        candidate, count = row[0], row[1]
                        if candidate in self.candidates[current_position]:
                            try:
                                votes[current_position][candidate] = int(count)
                            except ValueError:
                                print(f"Invalid vote count for {candidate}")
        except FileNotFoundError:
            print("No existing vote file found, starting fresh")
        return votes

    def write_votes(self, votes):
        """Write current vote counts to CSV file, including candidates with zero votes"""
        with open('votes.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for position in self.positions:
                writer.writerow([position])

                for candidate in self.candidates[position]:
                    count = votes[position].get(candidate, 0)  # Default to 0 if not found
                    writer.writerow([candidate, count])
                writer.writerow([])  # Add empty row between sections

    def process_vote(self, votes_data):
        """Process incoming votes and update counts"""
        votes = self.read_existing_votes()
        
        try:
            cb, cg, vcb, vcg = votes_data.split(',', 3)
            
            # Update counts for each position
            for position, candidate in zip(self.positions, [cb, cg, vcb, vcg]):
                if candidate in self.candidates[position]:
                    votes[position][candidate] += 1
                else:
                    print(f"Invalid candidate {candidate} for {position}")
            
            self.write_votes(votes)
            return True
            
        except Exception as e:
            print(f"Error processing vote: {e}")
            return False

    def start(self):
        """Start the voting server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")
            
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    try:
                        data = conn.recv(1024).decode('utf-8').strip()
                        if not data:
                            continue
                            
                        if self.process_vote(data):
                            conn.sendall(b"Votes counted successfully")
                        else:
                            conn.sendall(b"Error processing votes")
                            
                    except Exception as e:
                        print(f"Connection error: {e}")
                        conn.sendall(b"Server error occurred")

if __name__ == "__main__":
    server = VoteServer()
    server.start()
