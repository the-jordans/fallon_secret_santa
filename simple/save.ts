import { writeFileSync } from "fs"
import { SimpleResult } from "./hat"
import { Name } from "./data"


export const saveToFiles = (results: Array<SimpleResult>) => {
    const fallonSanta = theirSanta('Jordan Fallon', results)
    const haganSanta = theirSanta('Jordan Hagan', results)
    const theRest = results.filter(result => result.santa != fallonSanta.santa && result.santa != haganSanta.santa)

    const fallonNotes = [haganSanta]
        .concat(theRest.slice(0, 3))
        .map(result => `${result.santa} is getting a gift for ${result.receiver}`)
        .join('\n')

    const haganNotes = [fallonSanta]
        .concat(theRest.slice(3))
        .map(result => `${result.santa} is getting a gift for ${result.receiver}`)
        .join('\n')

    writeFileSync("hagan.txt", haganNotes)
    writeFileSync("fallon.txt", fallonNotes)
}

const theirSanta = (name: Name, results: Array<SimpleResult>) =>
    results.filter(result => result.receiver == name)[0]
