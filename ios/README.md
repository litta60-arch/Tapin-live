# iOS (SwiftUI) sample notes

This folder contains a minimal SwiftUI example showing how to connect to the backend token endpoint and then join LiveKit.

Requirements:
- Xcode 14+
- Swift Package: LiveKit (https://github.com/livekit/client-sdk-swift)

Example workflow:
1. Start backend and LiveKit (docker-compose up)
2. In your iOS app, call POST http://<backend-host>:8000/token with body {"identity":"user1","room":"roomA"}
3. Use the returned token with LiveKit's Connect/Room API in the iOS SDK.

See ContentView.swift for a minimal example.
