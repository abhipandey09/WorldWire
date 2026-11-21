import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Clock, CalendarCheck, Sparkles } from 'lucide-react';
import { WEDDING_EVENTS } from '../data/weddingData';
import { WeddingEvent } from '../types';

interface TimeLeft {
  days: number;
  hours: number;
  minutes: number;
  seconds: number;
  isComplete: boolean;
}

export const Countdown: React.FC = () => {
  const [activeEvent, setActiveEvent] = useState<WeddingEvent | null>(null);
  const [allCompleted, setAllCompleted] = useState<boolean>(false);
  const [timeLeft, setTimeLeft] = useState<TimeLeft>({
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0,
    isComplete: false,
  });

  useEffect(() => {
    const calculateTime = () => {
      const now = new Date().getTime();

      // Find the next upcoming event
      let nextEvent: WeddingEvent | null = null;
      for (const ev of WEDDING_EVENTS) {
        const eventTime = new Date(ev.isoDateTime).getTime();
        if (eventTime > now) {
          nextEvent = ev;
          break;
        }
      }

      if (!nextEvent) {
        // All events have begun or completed
        setAllCompleted(true);
        setActiveEvent(WEDDING_EVENTS[WEDDING_EVENTS.length - 1]);
        setTimeLeft({ days: 0, hours: 0, minutes: 0, seconds: 0, isComplete: true });
        return;
      }

      setAllCompleted(false);
      setActiveEvent(nextEvent);

      const targetTime = new Date(nextEvent.isoDateTime).getTime();
      const diff = targetTime - now;

      if (diff <= 0) {
        setTimeLeft({ days: 0, hours: 0, minutes: 0, seconds: 0, isComplete: true });
      } else {
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((diff / 1000 / 60) % 60);
        const seconds = Math.floor((diff / 1000) % 60);
        setTimeLeft({ days, hours, minutes, seconds, isComplete: false });
      }
    };

    calculateTime();
    const interval = setInterval(calculateTime, 1000);
    return () => clearInterval(interval);
  }, []);

  const timeUnits = [
    { label: 'DAYS', value: timeLeft.days },
    { label: 'HOURS', value: timeLeft.hours },
    { label: 'MINUTES', value: timeLeft.minutes },
    { label: 'SECONDS', value: timeLeft.seconds },
  ];

  return (
    <div className="relative z-20 max-w-4xl mx-auto px-4 sm:px-6">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.8 }}
        className="relative bg-ivory/95 rounded-2xl p-6 sm:p-8 border-2 border-gold/60 shadow-xl text-center backdrop-blur-sm overflow-hidden"
      >
        {/* Subtle decorative inner corner borders */}
        <div className="absolute inset-2 border border-gold/30 rounded-xl pointer-events-none" />

        {/* Section Header */}
        <div className="flex items-center justify-center gap-2 mb-1.5 text-gold">
          <Clock className="w-4 h-4 text-burgundy" />
          <span className="font-cinzel text-xs font-bold tracking-widest text-burgundy">
            COUNTING EVERY MOMENT UNTIL FOREVER
          </span>
          <Clock className="w-4 h-4 text-burgundy" />
        </div>

        {allCompleted ? (
          <div className="py-4">
            <div className="inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-burgundy text-white font-cinzel font-bold text-base sm:text-lg tracking-wider shadow-md">
              <Sparkles className="w-5 h-5 text-gold" />
              <span>The Celebration Has Begun! ✨</span>
            </div>
            <p className="mt-2 text-sm text-[#5C453C] font-cormorant italic">
              Thank you for being part of our cherished journey.
            </p>
          </div>
        ) : (
          <>
            {activeEvent && (
              <div className="mb-4">
                <span className="font-cormorant italic text-sm text-[#664E43]">
                  Next Auspicious Ceremony:
                </span>
                <h3 className="font-cinzel font-bold text-base sm:text-lg text-burgundy mt-0.5">
                  {activeEvent.name} &bull; {activeEvent.dateStr.split(',')[0]}
                </h3>
                <span className="text-xs text-gold font-semibold tracking-wider font-cinzel">
                  {activeEvent.timeStr} at {activeEvent.venueShort}
                </span>
              </div>
            )}

            {/* Countdown Clock Units */}
            <div className="grid grid-cols-4 gap-2 sm:gap-4 max-w-xl mx-auto my-2">
              {timeUnits.map((unit) => (
                <div
                  key={unit.label}
                  className="flex flex-col items-center justify-center p-2.5 sm:p-4 rounded-xl bg-gradient-to-b from-[#FFFDF9] to-champagne/40 border border-gold/50 shadow-sm"
                >
                  <span className="font-cinzel font-bold text-2xl sm:text-4xl text-burgundy tracking-tight">
                    {String(unit.value).padStart(2, '0')}
                  </span>
                  <span className="font-sans text-[9px] sm:text-[11px] font-semibold text-[#7D5F52] tracking-wider mt-1">
                    {unit.label}
                  </span>
                </div>
              ))}
            </div>

            <p className="font-cormorant italic text-xs sm:text-sm text-[#7D5F52] mt-3">
              Standard Time: Asia/Kolkata (IST &bull; UTC+05:30)
            </p>
          </>
        )}
      </motion.div>
    </div>
  );
};
