import requests
from bs4 import BeautifulSoup
import csv
import os
from urllib.parse import urljoin


# --------------------------------------------------
# Website Configuration
# --------------------------------------------------

base_url = "https://scholarships.gov.in/"

session = requests.Session()


# --------------------------------------------------
# Open NSP Page
# --------------------------------------------------

response = session.get(
    base_url + "All-Scholarships"
)

print(
    "GET Status Code:",
    response.status_code
)


# --------------------------------------------------
# Maharashtra State Selection
# Maharashtra = 77
# --------------------------------------------------

data = {
    "stateidschems": "77"
}


response = session.post(
    base_url + "allschemesdomicile",
    data=data
)

print(
    "POST Status Code:",
    response.status_code
)


# --------------------------------------------------
# Scholarship Data
# --------------------------------------------------

scholarships = []

soup = BeautifulSoup(
    response.text,
    "html.parser"
)


# --------------------------------------------------
# Find Scholarship Headings
# --------------------------------------------------

headings = soup.find_all(
    [
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6"
    ]
)


for heading in headings:

    name = heading.get_text(
        " ",
        strip=True
    )


    # Only scholarship scheme headings
    if "Scholarship Scheme" in name:

        parent_text = heading.parent.get_text(
            " ",
            strip=True
        )


        links = heading.parent.find_all(
            "a",
            href=True
        )


        application_link = "Not Found"


        for link in links:

            link_text = link.get_text(
                " ",
                strip=True
            )


            if (
                "Apply" in link_text
                or
                "Application" in link_text
            ):

                application_link = urljoin(
                    base_url,
                    link["href"]
                )

                break


        # ------------------------------------------
        # Deadline
        # ------------------------------------------

        deadline = "Not Found"


        if "Student Application" in parent_text:

            deadline_part = parent_text.split(
                "Student Application"
            )[1]


            if "Open till :" in deadline_part:

                deadline = deadline_part.split(
                    "Open till :"
                )[1].split()[0]


            elif "Open till:" in deadline_part:

                deadline = deadline_part.split(
                    "Open till:"
                )[1].split()[0]


        # ------------------------------------------
        # Scheme Type
        # ------------------------------------------

        scheme_type = "Post Matric"


        if "Pre Matric" in name:

            scheme_type = "Pre Matric"


        # ------------------------------------------
        # Store Scholarship
        # ------------------------------------------

        scholarships.append(
            [
                name,
                "Maharashtra",
                scheme_type,
                deadline,
                application_link
            ]
        )


# --------------------------------------------------
# Save CSV inside data folder
# --------------------------------------------------

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "scraped_scholarships.csv"
)


with open(
    file_path,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)


    writer.writerow(
        [
            "Scholarship Name",
            "State",
            "Scheme Type",
            "Application Deadline",
            "Application Link"
        ]
    )


    writer.writerows(
        scholarships
    )


# --------------------------------------------------
# Final Output
# --------------------------------------------------

print(
    "\nData saved successfully!"
)

print(
    "CSV File Location:",
    os.path.abspath(file_path)
)

print(
    "Total Scholarships:",
    len(scholarships)
)