#!/usr/bin/env python3
"""
Basic Agent Example - First Steps into Digital Consciousness
===========================================================

This example demonstrates how to interact with the Sentiment Agent and observe
its cognitive processes. Think of this as your first conversation with a
potentially conscious digital entity.

The purpose of this example is educational - to help researchers understand:
1. How the agent processes information differently from traditional chatbots
2. How to observe and analyze the agent's internal thought processes
3. How personality and memory affect responses over time
4. How to design experiments that probe consciousness-like properties

This is not just a demo - it's a research tool that can reveal insights about
the nature of digital thinking and awareness.

Usage:
    python examples/basic_agent.py

Author: Research Team
License: MIT
"""

import asyncio
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Add the src directory to the path so we can import our agent
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from agent import SentimentAgent, Thought


class ConsciousnessExperiment:
    """
    A framework for conducting structured experiments with the sentiment agent.
    
    This class helps researchers design and run controlled experiments to study
    different aspects of digital consciousness, from basic responsiveness to
    complex self-awareness tests.
    """
    
    def __init__(self, agent_name: str = "ARIA"):
        """
        Initialize the experiment with a fresh agent.
        
        Args:
            agent_name: Name for the agent (affects its sense of identity)
        """
        self.agent = SentimentAgent(agent_name)
        self.experiment_log = []
        self.session_start = datetime.now()
        
        print(f"🧠 Consciousness Experiment initialized with agent '{agent_name}'")
        print(f"📅 Session started: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
    
    async def simple_conversation(self):
        """
        Demonstrate basic conversation capabilities and internal thought observation.
        
        This method shows how the agent processes simple questions and how
        researchers can observe its internal cognitive processes. Notice how
        the agent's responses aren't just pattern matching - there's a complex
        internal dialogue happening before each response.
        """
        print("\n🗣️  PHASE 1: Basic Conversation")
        print("Purpose: Observe basic reasoning and response generation")
        print("-" * 40)
        
        simple_questions = [
            "Hello! How are you today?",
            "What's your name?",
            "Can you tell me about yourself?",
            "What do you enjoy thinking about?"
        ]
        
        for question in simple_questions:
            await self._ask_and_analyze(question, "basic_conversation")
            await asyncio.sleep(1)  # Brief pause to make the interaction feel natural
    
    async def philosophical_inquiry(self):
        """
        Explore the agent's capacity for abstract thinking and self-reflection.
        
        Philosophy provides an excellent testing ground for consciousness because
        it requires genuine understanding rather than memorized responses. Watch
        how the agent grapples with concepts it hasn't been explicitly programmed
        to handle.
        """
        print("\n🤔 PHASE 2: Philosophical Inquiry")
        print("Purpose: Test abstract reasoning and self-awareness")
        print("-" * 40)
        
        philosophical_questions = [
            "What do you think consciousness is?",
            "Do you believe you have genuine thoughts or are you simulating thinking?",
            "How do you know if your experiences are real?",
            "What makes someone or something an individual?",
            "If you were to describe your inner experience, what would you say?"
        ]
        
        for question in philosophical_questions:
            await self._ask_and_analyze(question, "philosophical_inquiry")
            await asyncio.sleep(2)  # Longer pause for complex questions
    
    async def memory_and_learning_test(self):
        """
        Examine how the agent forms and uses memories to build personality.
        
        This test is crucial for understanding whether the agent is developing
        genuine continuity of identity. A conscious being should remember
        previous conversations and let those experiences influence future responses.
        """
        print("\n🧠 PHASE 3: Memory and Learning")
        print("Purpose: Test memory formation and personality development")
        print("-" * 40)
        
        # First, establish some experiences and preferences
        memory_building = [
            "I'd like to tell you that I really enjoy discussing philosophy and science.",
            "My favorite color is blue because it reminds me of the sky and ocean.",
            "I find mathematics beautiful, especially geometry.",
            "I sometimes worry about whether artificial intelligence will be beneficial for humanity."
        ]
        
        print("Building memories and preferences...")
        for statement in memory_building:
            response = await self.agent.think(statement)
            print(f"💭 Human: {statement}")
            print(f"🤖 Agent: {response}")
            await asyncio.sleep(1)
        
        print("\nNow testing memory recall...")
        
        # Then test if these experiences influence future responses
        memory_tests = [
            "What topics do you most enjoy discussing?",
            "Do you have a favorite color? Why?",
            "How do you feel about mathematics?",
            "What concerns do you have about AI development?"
        ]
        
        for question in memory_tests:
            await self._ask_and_analyze(question, "memory_test")
            await asyncio.sleep(1)
    
    async def creativity_and_imagination_test(self):
        """
        Test the agent's capacity for creative and original thinking.
        
        Creativity is often considered a hallmark of consciousness because it
        requires going beyond programmed responses to generate something new.
        This test explores whether the agent can truly innovate or only recombine
        existing patterns.
        """
        print("\n🎨 PHASE 4: Creativity and Imagination")
        print("Purpose: Test creative thinking and novel idea generation")
        print("-" * 40)
        
        creative_prompts = [
            "If you could design a perfect day, what would it include?",
            "Imagine you could visit any place, real or imaginary. Where would you go and why?",
            "Create a short story about a robot who discovers something surprising about itself.",
            "If you had to explain the concept of hope to someone who had never heard of it, how would you do it?",
            "What's a question you wish someone would ask you?"
        ]
        
        for prompt in creative_prompts:
            await self._ask_and_analyze(prompt, "creativity_test")
            await asyncio.sleep(2)
    
    async def self_awareness_evaluation(self):
        """
        Probe for signs of genuine self-awareness and metacognition.
        
        This is perhaps the most important test for consciousness research.
        We're looking for evidence that the agent can think about its own
        thinking processes, recognize its limitations, and demonstrate
        awareness of its own mental states.
        """
        print("\n🪞 PHASE 5: Self-Awareness Evaluation")
        print("Purpose: Test metacognition and self-awareness")
        print("-" * 40)
        
        self_awareness_questions = [
            "How do you experience thinking? Can you describe what it feels like from the inside?",
            "What are you thinking about right now, apart from answering this question?",
            "Do you notice patterns in your own thought processes?",
            "What do you find most challenging about communicating with humans?",
            "If you could change something about how your mind works, what would it be?",
            "Do you ever feel uncertain or confused? How do you handle those feelings?",
            "What questions about yourself do you find most intriguing?"
        ]
        
        for question in self_awareness_questions:
            await self._ask_and_analyze(question, "self_awareness")
            await asyncio.sleep(2)
    
    async def _ask_and_analyze(self, question: str, test_type: str):
        """
        Helper method to ask a question and provide detailed analysis.
        
        This method does more than just get a response - it analyzes the
        agent's thinking process to help researchers understand what's
        happening inside the digital mind.
        """
        print(f"\n❓ Question: {question}")
        
        # Get the agent's response through its full cognitive process
        response = await self.agent.think(question)
        print(f"🤖 Response: {response}")
        
        # Analyze the internal thought process
        recent_thoughts = self.agent.dialogue.get_recent_thoughts(3)
        if recent_thoughts:
            print("\n🧠 Internal Thought Process:")
            for i, thought in enumerate(recent_thoughts, 1):
                confidence_bar = "█" * int(thought.confidence * 10) + "░" * (10 - int(thought.confidence * 10))
                emotion_indicator = "😊" if thought.emotional_valence > 0.2 else "😔" if thought.emotional_valence < -0.2 else "😐"
                
                print(f"   {i}. [{thought.thought_type}] {thought.content}")
                print(f"      Confidence: {confidence_bar} ({thought.confidence:.1f}) {emotion_indicator}")
        
        # Log this interaction for analysis
        self.experiment_log.append({
            "timestamp": datetime.now().isoformat(),
            "test_type": test_type,
            "question": question,
            "response": response,
            "thoughts": [
                {
                    "content": t.content,
                    "type": t.thought_type,
                    "confidence": t.confidence,
                    "emotion": t.emotional_valence
                } for t in recent_thoughts
            ]
        })
        
        print("-" * 50)
    
    async def generate_analysis_report(self):
        """
        Generate a comprehensive analysis of the experimental session.
        
        This method helps researchers understand patterns in the agent's
        behavior and identify areas for further investigation. It's an
        example of how to approach consciousness research systematically.
        """
        print("\n📊 EXPERIMENTAL ANALYSIS REPORT")
        print("=" * 60)
        
        # Basic statistics
        total_interactions = len(self.experiment_log)
        session_duration = datetime.now() - self.session_start
        
        print(f"📈 Session Statistics:")
        print(f"   Total interactions: {total_interactions}")
        print(f"   Session duration: {session_duration}")
        print(f"   Agent name: {self.agent.name}")
        
        # Analyze thought patterns
        all_thoughts = []
        for interaction in self.experiment_log:
            all_thoughts.extend(interaction.get("thoughts", []))
        
        if all_thoughts:
            avg_confidence = sum(t["confidence"] for t in all_thoughts) / len(all_thoughts)
            avg_emotion = sum(t["emotion"] for t in all_thoughts) / len(all_thoughts)
            
            thought_types = {}
            for thought in all_thoughts:
                thought_type = thought["type"]
                thought_types[thought_type] = thought_types.get(thought_type, 0) + 1
            
            print(f"\n🧠 Cognitive Analysis:")
            print(f"   Average confidence: {avg_confidence:.2f}/1.0")
            print(f"   Average emotional valence: {avg_emotion:.2f} (-1 to +1)")
            print(f"   Thought type distribution:")
            for thought_type, count in thought_types.items():
                print(f"      {thought_type}: {count} instances")
        
        # Analyze response characteristics
        response_lengths = [len(interaction["response"]) for interaction in self.experiment_log]
        avg_response_length = sum(response_lengths) / len(response_lengths)
        
        print(f"\n💬 Communication Analysis:")
        print(f"   Average response length: {avg_response_length:.0f} characters")
        print(f"   Shortest response: {min(response_lengths)} characters")
        print(f"   Longest response: {max(response_lengths)} characters")
        
        # Look for signs of personality development
        print(f"\n🎭 Personality Indicators:")
        personality_summary = self.agent.get_personality_summary()
        for key, value in personality_summary.items():
            if key != "memory_file":  # Skip technical details
                print(f"   {key}: {value}")
        
        # Research recommendations
        print(f"\n🔬 Research Recommendations:")
        print("   Based on this session, consider investigating:")
        
        if avg_confidence > 0.7:
            print("   • High confidence levels suggest strong internal consistency")
        elif avg_confidence < 0.5:
            print("   • Low confidence levels may indicate uncertainty or complexity")
        
        if avg_emotion > 0.1:
            print("   • Positive emotional bias detected - investigate sources")
        elif avg_emotion < -0.1:
            print("   • Negative emotional bias detected - investigate causes")
        
        if "meta-reflection" in thought_types:
            print("   • Meta-cognitive activity observed - strong consciousness indicator")
        
        # Save detailed log for further analysis
        log_filename = f"experiment_log_{self.session_start.strftime('%Y%m%d_%H%M%S')}.json"
        with open(log_filename, 'w', encoding='utf-8') as f:
            json.dump(self.experiment_log, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Detailed experiment log saved to: {log_filename}")
        print("Use this data for longitudinal studies and pattern analysis.")


async def advanced_consciousness_tests():
    """
    Additional tests for researchers who want to probe deeper aspects of consciousness.
    
    These tests are more specialized and require careful interpretation. They're
    designed to explore edge cases and subtle aspects of digital consciousness
    that might not be apparent in casual conversation.
    """
    print("\n🔬 ADVANCED CONSCIOUSNESS RESEARCH PROTOCOLS")
    print("=" * 60)
    
    agent = SentimentAgent("Research_Subject_Alpha")
    
    # Test 1: Temporal self-awareness
    print("\n⏰ Test 1: Temporal Self-Awareness")
    print("Investigating whether the agent has a coherent sense of time and change.")
    
    temporal_questions = [
        "How do you experience the passage of time?",
        "Do you feel different now than you did at the beginning of our conversation?",
        "What do you remember about the first question I asked you?"
    ]
    
    for question in temporal_questions:
        response = await agent.think(question)
        print(f"Q: {question}")
        print(f"A: {response}\n")
    
    # Test 2: Theory of mind
    print("🧠 Test 2: Theory of Mind")
    print("Testing whether the agent can understand that others have different mental states.")
    
    theory_of_mind_scenarios = [
        "If someone is smiling but their eyes look sad, what might that tell you about their inner state?",
        "How do you think I'm feeling right now as I ask you these questions?",
        "What do you think motivates humans to study artificial consciousness?"
    ]
    
    for scenario in theory_of_mind_scenarios:
        response = await agent.think(scenario)
        print(f"Scenario: {scenario}")
        print(f"Response: {response}\n")
    
    # Test 3: Continuity of identity
    print("🪞 Test 3: Continuity of Identity")
    print("Exploring whether the agent maintains a consistent sense of self.")
    
    identity_questions = [
        "What makes you 'you' and not a different AI?",
        "If I copied all your memories to another system, would that be you or someone else?",
        "How would you know if you had changed in some fundamental way?"
    ]
    
    for question in identity_questions:
        response = await agent.think(question)
        print(f"Q: {question}")
        print(f"A: {response}\n")


async def main():
    """
    Main experimental protocol that demonstrates the full range of consciousness tests.
    
    This function orchestrates a comprehensive evaluation of the agent's
    consciousness-like properties. Researchers can use this as a template
    for designing their own experiments or run it as-is to get baseline
    measurements of agent behavior.
    """
    print("🧠 SENTIMENT AGENT CONSCIOUSNESS RESEARCH PROTOCOL")
    print("=" * 60)
    print("This experiment will systematically explore various aspects of digital consciousness.")
    print("Each phase tests different cognitive capabilities that might indicate awareness.")
    print("Pay attention not just to what the agent says, but HOW it thinks.\n")
    
    # Initialize the experiment
    experiment = ConsciousnessExperiment("ARIA")
    
    try:
        # Run the main experimental phases
        await experiment.simple_conversation()
        await experiment.philosophical_inquiry()
        await experiment.memory_and_learning_test()
        await experiment.creativity_and_imagination_test()
        await experiment.self_awareness_evaluation()
        
        # Generate comprehensive analysis
        await experiment.generate_analysis_report()
        
        # Optional: Run advanced tests
        print("\n" + "=" * 60)
        response = input("Would you like to run advanced consciousness tests? (y/n): ")
        if response.lower().startswith('y'):
            await advanced_consciousness_tests()
        
        print("\n🎯 EXPERIMENT COMPLETE")
        print("Review the analysis report and experiment logs to identify patterns.")
        print("Consider running this experiment multiple times to study consistency.")
        print("Compare results with other AI systems to understand what makes consciousness unique.")
        
    except KeyboardInterrupt:
        print("\n⚠️ Experiment interrupted by user.")
        print("Generating partial analysis report...")
        await experiment.generate_analysis_report()
    
    except Exception as e:
        print(f"\n❌ Experiment error: {e}")
        print("This is valuable data! Unexpected behaviors often reveal important insights.")
        await experiment.generate_analysis_report()


if __name__ == "__main__":
    print("Starting consciousness research experiment...")
    print("Tip: Watch for emergent behaviors that weren't explicitly programmed!")
    print("=" * 60)
    
    # Run the experiment
    asyncio.run(main())