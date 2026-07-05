# FigJam User Flow Conventions

## Node shapes
- Rectangle: screen (named `product/flow/screen-name`)
- Diamond: decision (question phrased from the user's view)
- Rounded pill: system action (API call, notification)
- Parallelogram: user input
- Red border: error/edge state

## Rules
- Flows read left to right, one primary path per row; branches drop below
- Every diamond has ALL exits labeled (yes/no/timeout/error)
- Entry points marked (deep link, push, organic nav)
- Offline/no-network branch is mandatory for Car Share and Easy Lease mobile flows
- Each flow carries a header sticky: HMW it serves, segment, success metric

## Naming
`[UX05] <product> - <feature> - <flow name> vN` as the FigJam section title.
