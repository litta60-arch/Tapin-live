import SwiftUI
import LiveKitClient

struct ContentView: View {
    @State private var token: String = ""
    @State private var room: Room? = nil

    var body: some View {
        VStack(spacing: 20) {
            Button("Get Token and Join") {
                Task {
                    await getTokenAndJoin()
                }
            }
            if room != nil {
                Text("Joined room")
            }
        }
        .padding()
    }

    func getTokenAndJoin() async {
        guard let url = URL(string: "http://127.0.0.1:8000/token") else { return }
        var req = URLRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        let body = ["identity": "ios-user", "room": "test-room"]
        req.httpBody = try? JSONSerialization.data(withJSONObject: body)
        do {
            let (data, _) = try await URLSession.shared.data(for: req)
            if let json = try JSONSerialization.jsonObject(with: data) as? [String:Any],
               let t = json["token"] as? String {
                self.token = t
                // Connect to LiveKit
                let url = "http://127.0.0.1:7880" // LiveKit server url
                let engine = DefaultEngine(delegate: nil)
                let roomOptions = RoomOptions()
                let room = try await engine.connect(url: url, token: t, options: roomOptions)
                DispatchQueue.main.async {
                    self.room = room
                }
            }
        } catch {
            print("error fetching token", error)
        }
    }
}
