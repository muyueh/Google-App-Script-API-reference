## Calendar

### Methods

- createAllDayEvent(title, date) — CalendarEvent
- createAllDayEvent(title, startDate, endDate) — CalendarEvent
- createAllDayEvent(title, startDate, endDate, options) — CalendarEvent
- createAllDayEvent(title, date, options) — CalendarEvent
- createAllDayEventSeries(title, startDate, recurrence) — CalendarEventSeries
- createAllDayEventSeries(title, startDate, recurrence, options) — CalendarEventSeries
- createEvent(title, startTime, endTime) — CalendarEvent
- createEvent(title, startTime, endTime, options) — CalendarEvent
- createEventFromDescription(description) — CalendarEvent
- createEventSeries(title, startTime, endTime, recurrence) — CalendarEventSeries
- createEventSeries(title, startTime, endTime, recurrence, options) — CalendarEventSeries
- deleteCalendar() — void
- getColor() — String
- getDescription() — String
- getEventById(iCalId) — CalendarEvent
- getEventSeriesById(iCalId) — CalendarEventSeries
- getEvents(startTime, endTime) — CalendarEvent[]
- getEvents(startTime, endTime, options) — CalendarEvent[]
- getEventsForDay(date) — CalendarEvent[]
- getEventsForDay(date, options) — CalendarEvent[]
- getId() — String
- getName() — String
- getTimeZone() — String
- isHidden() — Boolean
- isMyPrimaryCalendar() — Boolean
- isOwnedByMe() — Boolean
- isSelected() — Boolean
- setColor(color) — Calendar
- setDescription(description) — Calendar
- setHidden(hidden) — Calendar
- setName(name) — Calendar
- setSelected(selected) — Calendar
- setTimeZone(timeZone) — Calendar
- unsubscribeFromCalendar() — void
