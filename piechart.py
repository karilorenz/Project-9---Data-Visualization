import matplotlib.pyplot as plt


labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
sizes = [33, 52, 12, 17, 62, 48]
# Make different pieces dominate, tuple --> amount want to each piece out
separated = (.1, 0, 0, 0, 0, 0)

# Pie Chart --> data, labels, percent,
plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)

# Keep chart aspect ratio
plt.axis('equal')

plt.show()