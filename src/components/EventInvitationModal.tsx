import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, Download, Share2, Calendar } from 'lucide-react';
import { WeddingEvent } from '../types';

interface EventInvitationModalProps {
  event: WeddingEvent | null;
  onClose: () => void;
  onOpenCalendar: (event: WeddingEvent) => void;
}

export const EventInvitationModal: React.FC<EventInvitationModalProps> = ({
  event,
  onClose,
  onOpenCalendar,
}) => {
  if (!event) return null;

  const handleShare = async () => {
    if (navigator.share) {
      try {
        await navigator.share({
          title: `${event.name} - Sakshi & Abhishek Wedding`,
          text: `${event.name} on ${event.dateStr} at ${event.venueName}.`,
          url: window.location.href,
        });
      } catch (err) {
        // User dismissed share
      }
    } else {
      navigator.clipboard.writeText(window.location.href);
      alert('Invitation link copied to clipboard!');
    }
  };

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/80 backdrop-blur-md overflow-y-auto">
        <motion.div
          initial={{ opacity: 0, scale: 0.94 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 0.94 }}
          transition={{ duration: 0.3 }}
          className="relative w-full max-w-lg bg-ivory rounded-2xl overflow-hidden border-2 border-gold shadow-2xl my-auto"
        >
          {/* Header Bar */}
          <div className="flex items-center justify-between px-5 py-3.5 bg-burgundy text-white border-b border-gold/40">
            <div className="flex flex-col">
              <span className="font-cinzel font-bold text-xs sm:text-sm tracking-wider text-gold">
                OFFICIAL INVITATION CARD
              </span>
              <span className="text-[11px] text-white/80 font-sans">{event.name}</span>
            </div>
            <button
              onClick={onClose}
              className="p-1 rounded-full text-gold hover:bg-gold/20 transition-colors"
              aria-label="Close modal"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* High-Resolution Invitation Card Image */}
          <div className="relative p-3 sm:p-4 bg-gradient-to-b from-[#2B1B15] to-[#120B09] flex items-center justify-center">
            <div className="relative max-h-[70vh] rounded-xl overflow-hidden shadow-2xl border border-gold/40">
              <img
                src={event.cardImage}
                alt={`${event.name} Invitation`}
                className="w-full h-auto max-h-[68vh] object-contain rounded-lg"
              />
            </div>
          </div>

          {/* Action Bar */}
          <div className="p-4 bg-ivory flex flex-wrap items-center justify-between gap-2 border-t border-gold/30">
            <button
              onClick={() => {
                onClose();
                onOpenCalendar(event);
              }}
              className="flex-1 flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl bg-champagne hover:bg-gold/20 border border-gold/60 text-burgundy font-cinzel font-bold text-xs tracking-wider transition-all"
            >
              <Calendar className="w-4 h-4 text-burgundy" />
              <span>Add to Calendar</span>
            </button>

            <a
              href={event.cardImage}
              download={`${event.id}_invitation_card.jpg`}
              className="flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl bg-burgundy hover:bg-burgundy/90 text-white font-cinzel font-bold text-xs tracking-wider transition-all"
            >
              <Download className="w-4 h-4 text-gold" />
              <span>Save Card</span>
            </a>

            <button
              onClick={handleShare}
              className="p-2.5 rounded-xl bg-champagne hover:bg-gold/20 border border-gold/60 text-burgundy transition-all"
              title="Share Invitation"
            >
              <Share2 className="w-4 h-4" />
            </button>
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
};
