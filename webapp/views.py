from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader # Not strictly needed if using render, but kept if you have other uses.

# Import your utility to read Excel data
from .utils import read_excel_table_data

# Helper to get table data and its headers
def get_table_context(file_name, table_number, table_title, sheet_name=None):
    """Reads excel data and prepares context for a table."""
    data = read_excel_table_data(file_name, sheet_name=sheet_name)
    headers = list(data[0].keys()) if data else []
    return {
        'data': data,
        'headers': headers,
        'title': f"Table {table_number}: {table_title}"
    }

# Your homepage view
def index(request):
    """
    View function for the homepage.
    Assumes your index.html is in templates
    """
    return render(request, 'index.html')

# Your 'About Us' page view
def about(request):
    """
    View function for the 'About Us' page.
    """
    return render(request, 'about.html')

# Your 'Applications' page view - now including all Excel data loading
def applications(request): # Renamed applications_page_view to applications for clarity
    """
    View function for the 'Applications' page.
    This view loads data from various Excel files to display tables.
    """
    context = {}

    # Read data for Agriculture/Horticulture Department (Table 1)
    context['agri_projects_table'] = get_table_context(
        'table1_agri_rd.xlsx',
        '1',
        'List of projects wherein outputs are used by Agriculture/Rural Development/Planning/Revenue/Disaster Management'
    )

    # Read data for Forest Department (Table 2)
    context['forest_projects_table'] = get_table_context(
        'table2_forest.xlsx',
        '2',
        'List of projects beneficial for the Forest Department'
    )

    # Read data for Environment Department (Table 3)
    context['environment_projects_table'] = get_table_context(
        'table3_environment.xlsx',
        '3',
        'List of projects beneficial for the Environment Department'
    )

    # Read data for Watershed Development & Soil Conservation Department (Table 4)
    context['watershed_projects_table'] = get_table_context(
        'table4_watershed.xlsx',
        '4',
        'List of projects beneficial for the Watershed Development & Soil Conservation Department'
    )
    
    # Read data for Water Resources Department (Table 5)
    context['water_resources_projects_table'] = get_table_context(
        'table5_water_resources.xlsx',
        '5',
        'List of projects beneficial for the Water Resources Department'
    )

    # Read data for Public Health Engineering Department (Table 6)
    context['public_health_projects_table'] = get_table_context(
        'table6_public_health.xlsx',
        '6',
        'List of projects beneficial for the Public Health Engineering Department'
    )

    # Read data for Ground Water Department (Table 7)
    context['ground_water_projects_table'] = get_table_context(
        'table7_ground_water.xlsx',
        '7',
        'List of projects beneficial for the Ground Water Department'
    )

    # Read data for Public Works Department (Table 8)
    context['public_works_projects_table'] = get_table_context(
        'table8_public_works.xlsx',
        '8',
        'List of projects beneficial for the Public Works Department'
    )

    # Read data for Rural Development and Panchayati Raj Department (Table 9)
    context['rural_dev_projects_table'] = get_table_context(
        'table9_rural_dev.xlsx',
        '9',
        'List of projects beneficial for the Rural Development and Panchayati Raj Department'
    )
    
    # Read data for Settlement Department/Board of Revenue (Table 10)
    context['settlement_projects_table'] = get_table_context(
        'table10_settlement.xlsx',
        '10',
        'List of projects beneficial for the Settlement Department'
    )

    # Read data for Urban Development & Housing Department (Table 11)
    context['urban_dev_projects_table'] = get_table_context(
        'table11_urban_dev.xlsx',
        '11',
        'List of projects beneficial for the Urban Development & Housing Department'
    )

    # Read data for Mines and Geology Department (Table 12)
    context['mines_geology_projects_table'] = get_table_context(
        'table12_mines_geology.xlsx',
        '12',
        'List of projects beneficial for the Mines and Geology Department'
    )

    # Read data for Planning Department (Table 2.13, using '13' for filename consistency)
    context['planning_projects_table'] = get_table_context(
        'table13_planning.xlsx', # Assuming you name the file 'table13_planning.xlsx'
        '2.13', # Display this as the table number in HTML
        'List of projects beneficial for the Planning Department'
    )

    return render(request, 'applications.html', context)

