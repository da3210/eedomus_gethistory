CREATE TABLE [dbo].[devices](
	[periph_id] [nvarchar](50) NOT NULL,
	[name] [nvarchar](100) NULL,
	[keep_history] [bit] NULL,
 CONSTRAINT [PK_devices2] PRIMARY KEY CLUSTERED 
(
	[periph_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]


CREATE TABLE [dbo].[History](
	[periph_id] [nvarchar](50) NOT NULL,
	[date] [nvarchar](50) NOT NULL,
	[value] [nvarchar](50) NULL,
 CONSTRAINT [PK_History] PRIMARY KEY CLUSTERED 
(
	[periph_id] ASC,
	[date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
