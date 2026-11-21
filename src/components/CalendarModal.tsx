import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, Calendar as CalendarIcon, Download, ExternalLink, Check } from 'lucide-react';
import { WeddingEvent } from '../types';
import { getGoogleCalendarUrl, getOutlookCalendarUrl, downloadIcsFile } from '../data/weddingData';

interface CalendarModalProps {
  event: WeddingEvent | null;
  onClose: () => void;
}

export const CalendarModal: React.FC<CalendarModalProps> = ({ event, onClose }) => {
  if (!event) return null;

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 20 }}
          className="relative w-full max-w-md bg-ivory rounded-2xl p-6 border-2 border-gold/70 shadow-2xl"
        >
          {/* Close Button */}
          <button
            onClick={onClose}
            className="absolute top-4 right-4 p-1.5 rounded-full text-[#6E4F41] hover:text-burgundy hover:bg-gold/10 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>

          {/* Modal Header */}
          <div className="flex items-center gap-2 text-burgundy mb-1">
            <CalendarIcon className="w-5 h-5 text-gold" />
            <span className="font-cinzel font-bold text-xs tracking-widest uppercase">
              Add Ceremony to Calendar
            </span>
          </div>
          <h3 className="font-serif font-bold text-xl text-burgundy">
            {event.name}
          </h3>
          <p className="text-xs text-[#705549] mt-0.5 mb-4">
            {event.dateStr} &bull; {event.timeStr}
          </p>

          {/* Calendar Service Options */}
          <div className="flex flex-col gap-2.5">
            {/* Google Calendar */}
            <a
              href={getGoogleCalendarUrl(event)}
              target="_blank"
              rel="noopener noreferrer"
              onClick={onClose}
              className="flex items-center justify-between px-4 py-3 rounded-xl bg-white hover:bg-champagne/40 border border-gold/40 shadow-sm transition-all group"
            >
              <div className="flex items-center gap-3">
                <span className="text-xl">📅</span>
                <div className="text-left">
                  <div className="font-cinzel font-bold text-xs text-burgundy">Google Calendar</div>
                  <div className="text-[11px] text-[#705549]">Sync directly with Google on web / Android</div>
                </div>
              </div>
              <ExternalLink className="w-4 h-4 text-gold group-hover:translate-x-0.5 transition-transform" />
            </a>

            {/* Apple Calendar / iCal (.ics) */}
            <button
              onClick={() => {
                downloadIcsFile(event);
                onClose();
              }}
              className="flex items-center justify-between px-4 py-3 rounded-xl bg-white hover:bg-champagne/40 border border-gold/40 shadow-sm transition-all group"
            >
              <div className="flex items-center gap-3">
                <span className="text-xl">🍏</span>
                <div className="text-left">
                  <div className="font-cinzel font-bold text-xs text-burgundy">Apple Calendar (.ics)</div>
                  <div className="text-[11px] text-[#705549]">Download file for iPhone, iPad &amp; Mac</div>
                </div>
              </div>
              <Download className="w-4 h-4 text-gold group-hover:translate-y-0.5 transition-transform" />
            </button>

            {/* Outlook Calendar */}
            <a
              href={getOutlookCalendarUrl(event)}
              target="_blank"
              rel="noopener noreferrer"
              onClick={onClose}
              className="flex items-center justify-between px-4 py-3 rounded-xl bg-white hover:bg-champagne/40 border border-gold/40 shadow-sm transition-all group"
            >
              <div className="flex items-center gap-3">
                <span className="text-xl">✉️</span>
                <div className="text-left">
                  <div className="font-cinzel font-bold text-xs text-burgundy">Outlook Online</div>
                  <div className="text-[11px] text-[#705549]">Add to Microsoft Outlook calendar</div>
                </div>
              </div>
              <ExternalLink className="w-4 h-4 text-gold group-hover:translate-x-0.5 transition-transform" />
            </a>
          </div>

          <div className="mt-4 pt-3 border-t border-gold/30 text-center text-[11px] text-[#8C6D60] font-sans">
            Timezone automatically mapped to <span className="font-semibold text-burgundy">Asia/Kolkata (IST)</span>.
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
};
