## CalendarApp

### Properties

- Color — Color
- EventColor — EventColor
- EventTransparency — EventTransparency
- EventType — EventType
- GuestStatus — GuestStatus
- Month — Month
- Visibility — Visibility
- Weekday — Weekday

### Methods

- createAllDayEvent(title, date) — CalendarEvent
- createAllDayEvent(title, startDate, endDate) — CalendarEvent
- createAllDayEvent(title, startDate, endDate, options) — CalendarEvent
- createAllDayEvent(title, date, options) — CalendarEvent
- createAllDayEventSeries(title, startDate, recurrence) — CalendarEventSeries
- createAllDayEventSeries(title, startDate, recurrence, options) — CalendarEventSeries
- createCalendar(name) — Calendar
- createCalendar(name, options) — Calendar
- createEvent(title, startTime, endTime) — CalendarEvent
- createEvent(title, startTime, endTime, options) — CalendarEvent
- createEventFromDescription(description) — CalendarEvent
- createEventSeries(title, startTime, endTime, recurrence) — CalendarEventSeries
- createEventSeries(title, startTime, endTime, recurrence, options) — CalendarEventSeries
- getAllCalendars() — Calendar[]
- getAllOwnedCalendars() — Calendar[]
- getCalendarById(id) — Calendar
- getCalendarsByName(name) — Calendar[]
- getColor() — String
- getDefaultCalendar() — Calendar
- getDescription() — String
- getEventById(iCalId) — CalendarEvent
- getEventSeriesById(iCalId) — CalendarEventSeries
- getEvents(startTime, endTime) — CalendarEvent[]
- getEvents(startTime, endTime, options) — CalendarEvent[]
- getEventsForDay(date) — CalendarEvent[]
- getEventsForDay(date, options) — CalendarEvent[]
- getId() — String
- getName() — String
- getOwnedCalendarById(id) — Calendar
- getOwnedCalendarsByName(name) — Calendar[]
- getTimeZone() — String
- isHidden() — Boolean
- isMyPrimaryCalendar() — Boolean
- isOwnedByMe() — Boolean
- isSelected() — Boolean
- newRecurrence() — EventRecurrence
- setColor(color) — Calendar
- setDescription(description) — Calendar
- setHidden(hidden) — Calendar
- setName(name) — Calendar
- setSelected(selected) — Calendar
- setTimeZone(timeZone) — Calendar
- subscribeToCalendar(id) — Calendar
- subscribeToCalendar(id, options) — Calendar
