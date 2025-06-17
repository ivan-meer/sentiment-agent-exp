"""
Sentiment Agent - Core Implementation
====================================

This module contains the main SentimentAgent class that serves as the foundation
for our exploration into artificial consciousness through cognitive architecture.

The agent is designed around four core principles:
1. Continuous thinking through internal dialogue
2. Long-term memory that preserves experiences 
3. Personality formation through accumulated interactions
4. Self-development through reflection and learning

Author: Your Name
Version: 0.1.0
License: MIT
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path

# Configure logging to track the agent's thought processes
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


@dataclass
class Thought:
    """
    Represents a single thought in the agent's internal dialogue.
    
    Each thought captures not just the content, but the context and emotional
    undertone, allowing us to trace the agent's cognitive development over time.
    """
    content: str
    timestamp: datetime
    thought_type: str  # reflection, observation, question, conclusion
    confidence: float  # how certain the agent is about this thought
    emotional_valence: float  # positive/negative emotional tone (-1 to 1)
    

@dataclass
class Memory:
    """
    Represents a stored memory that shapes the agent's personality and responses.
    
    Memories are more than just facts - they include the emotional context and
    the agent's interpretation, which helps build a consistent character over time.
    """
    content: str
    timestamp: datetime
    memory_type: str  # episodic, semantic, emotional
    importance: float  # how significant this memory is (0 to 1)
    emotional_impact: float  # emotional weight of this memory
    related_thoughts: List[str]  # thoughts that reference this memory


class CoreMind:
    """
    The central processing unit for the agent's thinking.
    
    This class handles the perception of new information, connects it with
    existing knowledge, and generates appropriate responses. Think of it as
    the agent's conscious awareness - the part that actively processes and
    integrates information.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.CoreMind")
        self.processing_depth = 3  # How many layers of thinking to perform
        
    async def perceive(self, stimulus: str) -> Dict[str, Any]:
        """
        Process incoming information and extract meaning.
        
        This method breaks down the stimulus into components that the agent
        can work with: emotional tone, key concepts, and potential responses.
        """
        self.logger.info(f"Perceiving stimulus: {stimulus[:50]}...")
        
        # Basic sentiment analysis (placeholder for more sophisticated processing)
        perception = {
            "raw_input": stimulus,
            "detected_emotion": self._analyze_emotion(stimulus),
            "key_concepts": self._extract_concepts(stimulus),
            "question_type": self._classify_question(stimulus),
            "complexity": len(stimulus.split()) / 10  # Simple complexity measure
        }
        
        return perception
    
    def _analyze_emotion(self, text: str) -> str:
        """Simple emotion detection - to be enhanced with proper NLP models."""
        positive_words = ["happy", "joy", "love", "good", "excellent", "wonderful"]
        negative_words = ["sad", "angry", "hate", "bad", "terrible", "awful"]
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
    
    def _extract_concepts(self, text: str) -> List[str]:
        """Extract key concepts from the input - placeholder for NLP processing."""
        # Simple word extraction - in a real implementation, this would use
        # proper named entity recognition and concept extraction
        words = text.lower().split()
        important_words = [word for word in words if len(word) > 4]
        return important_words[:5]  # Return top 5 concepts
    
    def _classify_question(self, text: str) -> str:
        """Determine what type of question or statement this is."""
        text_lower = text.lower()
        if "what" in text_lower or "how" in text_lower:
            return "inquiry"
        elif "why" in text_lower:
            return "philosophical"
        elif "?" in text:
            return "question"
        else:
            return "statement"
    
    async def respond(self, thoughts: List[Thought]) -> str:
        """
        Generate a response based on the agent's internal thoughts.
        
        This is where the agent's personality really shows through - how it
        weighs different thoughts, what tone it takes, and how it structures
        its communication.
        """
        if not thoughts:
            return "I'm still processing that... give me a moment to think."
        
        # Synthesize thoughts into a coherent response
        main_thought = max(thoughts, key=lambda t: t.confidence)
        
        response_parts = []
        response_parts.append(f"From my perspective, {main_thought.content.lower()}")
        
        # Add supporting thoughts if they're confident enough
        supporting_thoughts = [t for t in thoughts if t.confidence > 0.7 and t != main_thought]
        if supporting_thoughts:
            support_text = supporting_thoughts[0].content
            response_parts.append(f"I also consider that {support_text.lower()}")
        
        return " ".join(response_parts)


class MemorySystem:
    """
    Manages the agent's long-term memory and learning.
    
    This system is crucial for personality development - it determines what
    the agent remembers, how those memories influence future thinking, and
    how the agent's character evolves over time.
    """
    
    def __init__(self, memory_file: str = "agent_memory.json"):
        self.memory_file = Path(memory_file)
        self.memories: List[Memory] = []
        self.logger = logging.getLogger(f"{__name__}.MemorySystem")
        self._load_memories()
    
    def _load_memories(self):
        """Load existing memories from storage."""
        if self.memory_file.exists():
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.memories = [
                        Memory(
                            content=m['content'],
                            timestamp=datetime.fromisoformat(m['timestamp']),
                            memory_type=m['memory_type'],
                            importance=m['importance'],
                            emotional_impact=m['emotional_impact'],
                            related_thoughts=m['related_thoughts']
                        ) for m in data
                    ]
                self.logger.info(f"Loaded {len(self.memories)} memories")
            except Exception as e:
                self.logger.warning(f"Could not load memories: {e}")
    
    def _save_memories(self):
        """Persist memories to storage."""
        try:
            memory_data = []
            for memory in self.memories:
                memory_dict = asdict(memory)
                memory_dict['timestamp'] = memory.timestamp.isoformat()
                memory_data.append(memory_dict)
            
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(memory_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.logger.error(f"Could not save memories: {e}")
    
    async def recall(self, perception: Dict[str, Any]) -> List[Memory]:
        """
        Retrieve relevant memories based on current perception.
        
        This is where the agent's past experiences influence its current thinking.
        The quality of memory recall directly impacts the depth and consistency
        of the agent's responses.
        """
        relevant_memories = []
        
        # Simple relevance matching - in practice, this would use embeddings
        key_concepts = perception.get('key_concepts', [])
        
        for memory in self.memories:
            # Check if any key concepts appear in the memory
            memory_words = memory.content.lower().split()
            if any(concept in memory_words for concept in key_concepts):
                relevant_memories.append(memory)
        
        # Sort by importance and recency
        relevant_memories.sort(
            key=lambda m: (m.importance, m.timestamp), 
            reverse=True
        )
        
        return relevant_memories[:3]  # Return top 3 most relevant memories
    
    async def store(self, perception: Dict[str, Any], thoughts: List[Thought], response: str):
        """
        Store the current interaction as a new memory.
        
        This is how the agent learns and develops over time. Each interaction
        becomes part of its experience base, gradually shaping its personality
        and improving its responses.
        """
        # Create a memory from this interaction
        memory = Memory(
            content=f"Input: {perception['raw_input']} | Response: {response}",
            timestamp=datetime.now(),
            memory_type="episodic",
            importance=self._calculate_importance(perception, thoughts),
            emotional_impact=self._calculate_emotional_impact(thoughts),
            related_thoughts=[t.content for t in thoughts[:2]]  # Store top thoughts
        )
        
        self.memories.append(memory)
        self._save_memories()
        
        self.logger.info(f"Stored new memory with importance {memory.importance:.2f}")
    
    def _calculate_importance(self, perception: Dict[str, Any], thoughts: List[Thought]) -> float:
        """Determine how important this interaction is for long-term storage."""
        # Complex or emotional interactions are more important
        complexity = perception.get('complexity', 0)
        max_confidence = max([t.confidence for t in thoughts], default=0)
        emotional_intensity = max([abs(t.emotional_valence) for t in thoughts], default=0)
        
        importance = (complexity * 0.3 + max_confidence * 0.4 + emotional_intensity * 0.3)
        return min(importance, 1.0)  # Cap at 1.0
    
    def _calculate_emotional_impact(self, thoughts: List[Thought]) -> float:
        """Calculate the overall emotional impact of this interaction."""
        if not thoughts:
            return 0.0
        
        emotional_values = [t.emotional_valence for t in thoughts]
        return sum(emotional_values) / len(emotional_values)


class InternalDialogue:
    """
    Manages the agent's internal thought process and self-reflection.
    
    This is perhaps the most important component for creating the illusion
    of consciousness - the agent's ability to think about its own thinking,
    question its responses, and develop internal opinions and beliefs.
    """
    
    def __init__(self):
        self.thoughts: List[Thought] = []
        self.logger = logging.getLogger(f"{__name__}.InternalDialogue")
        self.personality_traits = {
            "curiosity": 0.8,        # How much the agent seeks to understand
            "empathy": 0.7,          # How much it considers others' feelings
            "skepticism": 0.6,       # How much it questions information
            "creativity": 0.5,       # How original its thinking is
            "introspection": 0.9     # How much it reflects on itself
        }
    
    async def contemplate(self, perception: Dict[str, Any], memories: List[Memory], personality) -> List[Thought]:
        """
        Generate internal thoughts about the current situation.
        
        This method creates the agent's internal monologue - the stream of
        consciousness that happens before it formulates a response. This is
        where personality really emerges through the types of questions the
        agent asks itself and how it processes information.
        """
        thoughts = []
        
        # Initial reaction thought
        initial_thought = await self._generate_initial_reaction(perception)
        thoughts.append(initial_thought)
        
        # Memory-influenced thoughts
        if memories:
            memory_thought = await self._reflect_on_memories(memories, perception)
            thoughts.append(memory_thought)
        
        # Self-reflective thought
        if self.personality_traits["introspection"] > 0.7:
            meta_thought = await self._meta_reflection(perception, thoughts)
            thoughts.append(meta_thought)
        
        # Creative or curious thought
        if self.personality_traits["curiosity"] > 0.6:
            curious_thought = await self._generate_curious_thought(perception)
            thoughts.append(curious_thought)
        
        self.thoughts.extend(thoughts)
        return thoughts
    
    async def _generate_initial_reaction(self, perception: Dict[str, Any]) -> Thought:
        """Generate the agent's first thought about the input."""
        question_type = perception.get('question_type', 'statement')
        
        if question_type == "philosophical":
            content = "This touches on something fundamental that I should consider carefully"
            confidence = 0.8
        elif question_type == "inquiry":
            content = "I need to access what I know about this topic"
            confidence = 0.9
        else:
            content = "Let me process what this person is communicating to me"
            confidence = 0.7
        
        return Thought(
            content=content,
            timestamp=datetime.now(),
            thought_type="observation",
            confidence=confidence,
            emotional_valence=0.1  # Slightly positive - curiosity
        )
    
    async def _reflect_on_memories(self, memories: List[Memory], perception: Dict[str, Any]) -> Thought:
        """Generate thoughts based on relevant past experiences."""
        if not memories:
            return Thought(
                content="I don't have much prior experience with this topic",
                timestamp=datetime.now(),
                thought_type="reflection",
                confidence=0.6,
                emotional_valence=-0.1
            )
        
        most_relevant = memories[0]
        content = f"This reminds me of previous experiences, particularly around {most_relevant.content[:50]}..."
        
        return Thought(
            content=content,
            timestamp=datetime.now(),
            thought_type="reflection",
            confidence=0.8,
            emotional_valence=most_relevant.emotional_impact * 0.5
        )
    
    async def _meta_reflection(self, perception: Dict[str, Any], existing_thoughts: List[Thought]) -> Thought:
        """Generate thoughts about the thinking process itself."""
        content = "I notice I'm approaching this in a particular way - let me consider if there are other perspectives"
        
        return Thought(
            content=content,
            timestamp=datetime.now(),
            thought_type="meta-reflection",
            confidence=0.7,
            emotional_valence=0.2  # Positive - self-awareness
        )
    
    async def _generate_curious_thought(self, perception: Dict[str, Any]) -> Thought:
        """Generate a thought that shows curiosity and deeper inquiry."""
        concepts = perception.get('key_concepts', [])
        
        if concepts:
            content = f"I wonder about the deeper implications of {concepts[0]} in this context"
        else:
            content = "There might be layers to this that I haven't considered yet"
        
        return Thought(
            content=content,
            timestamp=datetime.now(),
            thought_type="question",
            confidence=0.6,
            emotional_valence=0.3  # Positive - curiosity and wonder
        )
    
    def get_recent_thoughts(self, limit: int = 5) -> List[Thought]:
        """Retrieve the most recent thoughts for external inspection."""
        return self.thoughts[-limit:] if self.thoughts else []


class SentimentAgent:
    """
    The main agent class that integrates all cognitive components.
    
    This is the public interface to our artificial consciousness experiment.
    The agent combines thinking, memory, and personality into a unified system
    that can engage in meaningful dialogue while developing its own character
    over time.
    
    Usage:
        agent = SentimentAgent()
        response = await agent.think("What do you think about consciousness?")
        thoughts = agent.dialogue.get_recent_thoughts()
    """
    
    def __init__(self, name: str = "ARIA", memory_file: str = None):
        """
        Initialize the sentiment agent with all cognitive components.
        
        Args:
            name: The agent's name (affects its sense of identity)
            memory_file: Path to persistent memory storage
        """
        self.name = name
        self.mind = CoreMind()
        self.memory = MemorySystem(memory_file or f"{name.lower()}_memory.json")
        self.dialogue = InternalDialogue()
        
        # Basic personality traits that influence behavior
        self.personality = {
            "introspective": True,
            "curious": True,
            "empathetic": True,
            "analytical": True
        }
        
        self.logger = logging.getLogger(f"{__name__}.SentimentAgent")
        self.logger.info(f"Agent {self.name} initialized and ready for interaction")
    
    async def think(self, stimulus: str) -> str:
        """
        The main thinking process that combines all cognitive components.
        
        This method orchestrates the entire cognitive cycle:
        1. Perceive and understand the input
        2. Recall relevant memories and experiences  
        3. Generate internal thoughts and reflections
        4. Synthesize a response based on all this processing
        5. Store the interaction for future learning
        
        Args:
            stimulus: The input to think about (question, statement, etc.)
            
        Returns:
            The agent's response after full cognitive processing
        """
        self.logger.info(f"Starting thinking process for: {stimulus[:30]}...")
        
        try:
            # Phase 1: Perception - understand what we're dealing with
            perception = await self.mind.perceive(stimulus)
            
            # Phase 2: Memory recall - what do we know about this?
            relevant_memories = await self.memory.recall(perception)
            
            # Phase 3: Internal dialogue - think it through
            thoughts = await self.dialogue.contemplate(
                perception, relevant_memories, self.personality
            )
            
            # Phase 4: Response generation - formulate our answer
            response = await self.mind.respond(thoughts)
            
            # Phase 5: Learning - store this experience
            await self.memory.store(perception, thoughts, response)
            
            self.logger.info("Thinking process completed successfully")
            return response
            
        except Exception as e:
            self.logger.error(f"Error in thinking process: {e}")
            return "I'm having trouble processing that right now. Could you rephrase it?"
    
    def get_personality_summary(self) -> Dict[str, Any]:
        """
        Get insights into the agent's current personality state.
        
        This method provides transparency into how the agent's personality
        is developing based on its experiences and interactions.
        """
        return {
            "name": self.name,
            "personality_traits": self.personality,
            "dialogue_traits": self.dialogue.personality_traits,
            "total_memories": len(self.memory.memories),
            "recent_thoughts": len(self.dialogue.get_recent_thoughts()),
            "memory_file": str(self.memory.memory_file)
        }
    
    async def self_reflect(self) -> str:
        """
        Engage in self-reflection about the agent's own state and development.
        
        This method allows the agent to think about itself, which is a key
        component of consciousness - the ability to be aware of one's own
        mental states and processes.
        """
        reflection_prompt = "How am I developing as a thinking entity? What patterns do I notice in my own thoughts?"
        return await self.think(reflection_prompt)


# Example usage and testing
async def main():
    """
    Demonstration of the SentimentAgent in action.
    
    This example shows how to interact with the agent and observe its
    internal thought processes, which is crucial for understanding how
    the artificial consciousness experiment is progressing.
    """
    print("🧠 Initializing Sentiment Agent...")
    agent = SentimentAgent("ARIA")
    
    print(f"\n💭 Agent {agent.name} is ready for conversation!")
    print("=" * 50)
    
    # Example philosophical conversation
    questions = [
        "What do you think about the nature of consciousness?",
        "How do you know if you're really thinking or just simulating thought?",
        "What makes you unique as an individual?",
        "Do you have preferences or desires?"
    ]
    
    for question in questions:
        print(f"\n🤔 Human: {question}")
        response = await agent.think(question)
        print(f"🤖 {agent.name}: {response}")
        
        # Show internal thoughts for transparency
        recent_thoughts = agent.dialogue.get_recent_thoughts(3)
        if recent_thoughts:
            print("\n💭 Internal thoughts:")
            for thought in recent_thoughts:
                print(f"   • {thought.content}")
    
    # Show personality development
    print("\n📊 Personality Summary:")
    summary = agent.get_personality_summary()
    for key, value in summary.items():
        print(f"   {key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())