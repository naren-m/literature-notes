#!/usr/bin/env python3
"""
Background synthesis scheduler for Literature Notes Integration
Runs periodic knowledge synthesis and updates
"""

import time
import schedule
import logging
from datetime import datetime
from knowledge_synthesis import KnowledgeSynthesizer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_daily_synthesis():
    """Run daily knowledge synthesis"""
    logger.info("🧠 Starting scheduled daily synthesis...")
    
    try:
        synthesizer = KnowledgeSynthesizer()
        synthesis = synthesizer.generate_daily_synthesis()
        
        num_groups = len(synthesis.get('groups', []))
        num_insights = len(synthesis.get('insights', []))
        
        logger.info(f"✅ Daily synthesis completed:")
        logger.info(f"   - Knowledge clusters: {num_groups}")
        logger.info(f"   - Insights generated: {num_insights}")
        
        return synthesis
        
    except Exception as e:
        logger.error(f"❌ Daily synthesis failed: {e}")
        return None

def run_domain_analysis():
    """Run analysis of key domains"""
    logger.info("📊 Starting domain analysis...")
    
    domains = ['programming', 'sanskrit', 'ayurveda', 'cryptography', 'leadership']
    
    try:
        synthesizer = KnowledgeSynthesizer()
        
        for domain in domains:
            try:
                summary = synthesizer.generate_domain_summary(domain, max_notes=5)
                if summary.get('note_count', 0) > 0:
                    logger.info(f"   - {domain}: {summary['note_count']} notes, {summary['total_words']} words")
            except Exception as e:
                logger.warning(f"   - {domain}: Analysis failed - {e}")
                
        logger.info("✅ Domain analysis completed")
        
    except Exception as e:
        logger.error(f"❌ Domain analysis failed: {e}")

def health_check():
    """Simple health check"""
    logger.info("💓 Synthesis scheduler health check - OK")

def main():
    """Main scheduler loop"""
    logger.info("📅 Literature Notes Synthesis Scheduler Starting...")
    
    # Schedule tasks
    schedule.every().day.at("09:00").do(run_daily_synthesis)
    schedule.every().day.at("18:00").do(run_domain_analysis)
    schedule.every().hour.do(health_check)
    
    # Run initial synthesis
    logger.info("🚀 Running initial synthesis...")
    run_daily_synthesis()
    
    logger.info("⏰ Scheduler active - waiting for scheduled tasks...")
    
    # Main loop
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
            
        except KeyboardInterrupt:
            logger.info("🛑 Scheduler stopped by user")
            break
        except Exception as e:
            logger.error(f"❌ Scheduler error: {e}")
            time.sleep(60)  # Wait before retrying

if __name__ == "__main__":
    main()