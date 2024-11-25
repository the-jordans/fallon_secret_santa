export type Name =
    'Jan Fallon' | 'Chuck Fallon' |
    'Jordan Fallon' | 'Jordan Hagan' |
    'Gabe Fallon' | 'Jen Fallon' |
    'Micah Fallon' | 'Katie Fallon'

export type Person = {
    name: Name
    sigOther: Name
    history: Record<number, Name>
}

export const YEARS_THIS_CYCLE: Array<number> = []

export const family: Array<Person> = [
    {
        name: 'Jan Fallon',
        sigOther: 'Chuck Fallon',
        history: {
            2018: 'Gabe Fallon',
            2019: 'Jordan Fallon',
            2020: 'Katie Fallon',
            2021: 'Micah Fallon',
            2022: 'Jordan Hagan',
            2023: 'Jen Fallon',
        }
    },
    {
        name: 'Chuck Fallon',
        sigOther: 'Jan Fallon',
        history: {
            2018: 'Katie Fallon',
            2019: 'Jen Fallon',
            2020: 'Micah Fallon',
            2021: 'Jordan Hagan',
            2022: 'Gabe Fallon',
            2023: 'Jordan Fallon',
        }
    },
    {
        name: 'Jordan Fallon',
        sigOther: 'Jordan Hagan',
        history: {
            2018: 'Jen Fallon',
            2019: 'Gabe Fallon',
            2020: 'Jan Fallon',
            2021: 'Chuck Fallon',
            2022: 'Katie Fallon',
            2023: 'Micah Fallon',
        }
    },
    {
        name: 'Jordan Hagan',
        sigOther: 'Jordan Fallon',
        history: {
            2018: 'Micah Fallon',
            2019: 'Jan Fallon',
            2020: 'Jen Fallon',
            2021: 'Katie Fallon',
            2022: 'Chuck Fallon',
            2023: 'Gabe Fallon',
        }
    },
    {
        name: 'Gabe Fallon',
        sigOther: 'Jen Fallon',
        history: {
            2018: 'Chuck Fallon',
            2019: 'Katie Fallon',
            2020: 'Jordan Fallon',
            2021: 'Jan Fallon',
            2022: 'Micah Fallon',
            2023: 'Jordan Hagan',
        }
    },
    {
        name: 'Jen Fallon',
        sigOther: 'Gabe Fallon',
        history: {
            2018: 'Jordan Hagan',
            2019: 'Micah Fallon',
            2020: 'Chuck Fallon',
            2021: 'Jordan Fallon',
            2022: 'Jan Fallon',
            2023: 'Katie Fallon'
        }
    },
    {
        name: 'Micah Fallon',
        sigOther: 'Katie Fallon',
        history: {
            2018: 'Jordan Fallon',
            2019: 'Chuck Fallon',
            2020: 'Jordan Hagan',
            2021: 'Gabe Fallon',
            2022: 'Jen Fallon',
            2023: 'Jan Fallon',
        }
    },
    {
        name: 'Katie Fallon',
        sigOther: 'Micah Fallon',
        history: {
            2018: 'Jan Fallon',
            2019: 'Jordan Hagan',
            2020: 'Gabe Fallon',
            2021: 'Jen Fallon',
            2022: 'Jordan Fallon',
            2023: 'Chuck Fallon'
        }
    },
]
